import json


from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from . import models

def index( request ):
    return HttpResponse( "POST" )

class Messages( View ):
    model = models.Message

    def get( self, request, message_id=None ):
        # Check if the client requested all messages
        if message_id is None:
            messages = self.model.objects.all()
        else:
            # We need to ensure that the message id requested actually exists!
            try:
                messages = [ self.model.objects.get( pk=message_id ) ]
            except ObjectDoesNotExist:
                return JsonResponse( { 'errors' : { 'message_id' : 'Does not exist' } } )

        # Because the serialized data contains model information and pk, we don't want to expose it to
        # the client! Thus we loop on every Json object and extract everything that is not in the
        # "fields" section
        message_data = serializers.serialize( 'json', messages )
        message_data = json.loads( message_data )
        for index in range( len( message_data ) ):
            message_data[ index ] = message_data[ index ][ 'fields' ]

        message_data = json.dumps( message_data )

        # You might be wondering why use HttpResponse and not JsonResponse. This is because the
        # later only supports sending one JSON object. This also exposes you to content_type.
        return HttpResponse( message_data, content_type='application/json' )

    def post( self, request, message_id=None ):
        if message_id is not None:
            return JsonResponse( { 'errors' : { 'message_id' : 'cannot post using an existing id' } } )

        # From our earlier discussion, the client will only be sending us the information stored in
        # the models, the "internals" such as the pk and the model name/ class need to be filled in
        # by us.
        # In general, Django serializes to the following format:
        #   {
        #       "pk" : pk
        #       "model" : <app>.<model name>
        #       "Fields" : <dict of fields in model > <-- This is what the client cares about only
        #   }
        message_data = ( '[{{"model" : "irc.message", "pk" : null, '
                         '"fields" : {} }}]'.format( str( request.body, 'utf-8' ) ) )

        try:
            new_message = list( serializers.deserialize( "json", message_data ) )[ 0 ]
            # Validate Profile
            new_message.object.clean_fields()
            new_message.object.clean()
            # Create the profile
            new_message.save()
            # Inc the post of the owner
            new_message.object.profile.post_count += 1
            new_message.object.profile.save()
        except serializers.base.DeserializationError:
            raise
            return JsonResponse( { 'errors' : { 'payload' : 'Deserialization error!' } } )
        except ValidationError as e:
            return JsonResponse( { 'errors' : e.message_dict } )

        return JsonResponse( { 'id' : new_message.object.pk } )


class Profiles( View ):
    model = models.Profile

    def get( self, request, profile_id=None ):
        if profile_id is None:
            return JsonResponse( { 'errors' : { 'profile_id' : 'empty' } } )

        try:
            profile = self.model.objects.get( pk=profile_id )
        except ObjectDoesNotExist:
            return JsonResponse( { 'errors' : { 'profile_id' : 'not found'} } )

        # As above we have to filter out anything that is not in "Fields"
        data = serializers.serialize( 'json', [ profile, ] )
        data = json.loads( data )
        data = data[0][ 'fields' ]

        # Because we always know we are going to be returning one object here, we can use a
        # JsonResponse!
        return JsonResponse( data )

    def post( self, request, profile_id=None ):
        if profile_id is not None:
            return JsonResponse( { 'errors' : { 'profile_id' : 'cannot post using an existing id' } } )

        profile_data = ( '[{{"model" : "irc.profile", "pk" : null, '
                         ' "fields" : {} }}]'.format( str( request.body, 'utf-8' ) ) )

        try:
            new_profile = list( serializers.deserialize( 'json', str(profile_data) ) )[ 0 ]
            # Validate fields
            new_profile.object.clean_fields()
            new_profile.object.clean()
            # Create the profile
            new_profile.save()
        except serializers.base.DeserializationError:
            return JsonResponse( { 'errors' : { 'profile_id' : 'Deserialization error!' } } )
        except ValidationError as err:
            return JsonResponse( { 'errors' : err.message_dict, } )

        return JsonResponse( { 'id' : new_profile.object.pk } )

    def put( self, request, profile_id=None ):
        if profile_id is None:
            return JsonResponse( { 'errors' : { 'profile_id' : 'empty' } } )

        try:
            new_email = json.loads( request.body )[ 'email' ]
            profile = self.model.objects.get( pk=profile_id )
            profile.email = new_email
            profile.save()
        except ValidationError as e:
            return JsonResponse( { 'errors' : e.message_dict, } )

        return JsonResponse( { 'id' : profile_id } )
