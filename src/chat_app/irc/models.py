from django.db import models
from django.core.validators import EmailValidator

class Profile( models.Model ):
    name = models.CharField( max_length=25 )
    post_count = models.IntegerField( default=0 )
    email = models.CharField( max_length=100, validators=[ EmailValidator() ] )

class Message( models.Model ):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE )
    message_text = models.CharField( max_length=10000 )
    pub_date = models.DateTimeField( 'date published' )
