# 
## **Tutorial for creating RESTful backend**

<img src="media/backend.jpg" alt="drawing" />

---

# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- **What is REST and why to use it?**
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- What are alternate tools to build backend?

---

# What is REST

## REpresentational State Transfer

An **architectural style** for systems **to communicate on web**.

---
# What is REST

## Main Characteristics of an REST architectural style

---
# What is REST

# Main Characteristics of an REST architectural style

## Uniform Interface

for accessing server resources

- Identification of resources (URL).
- Manipulation of resources (use CRUD commands to manipulate).
- Self-descriptive messages (about Errors or Warnings or Success).

---

# What is REST

# Main Characteristics of an REST architectural style

## Stateless 

- Each request must contain all of the information necessary to understand the request.
- *Advantages*: Reliability is improved because it eases the task of recovering from partial failures of server.
- *Disadvantage*: It may decrease network performance (due to large packet sizes).

---

# What is REST

# Main Characteristics of an REST architectural style

## Cacheable

- Responses have to be capable of being labeled as cacheable or non-cacheable. 
- By labeling as cacheable, client cache is given the right to reuse that response data for later equivalent request.
- *Advantages*: eliminates some interactions, improves efficiency, scalability, and user-perceived performance.
- *Disadvantage*: decrease reliability if stale data within the cache differs significantly from the data that would have been obtained had the request been sent directly to the server.
---

# What is REST

# Main Characteristics of an REST architectural style

## Pull-based interaction style

- Only emitting a notification upon receipt of a request
- Although this is less efficient when viewed as a single client wishing to monitor a single resource, the scale of the Web makes an unregulated push model infeasible

---

# Why to use REST ? Advantages

- Code one API and build as many types of clients (web, mobile web, phone, tablet) you want (due to uniform Interface of REST)
- Scalable (as you cache and servers only have to respond to requests)
- Reliable (as it is stateless, don't have to worry about server failures)

---
# Agenda

Introduction to create a simple REST back-end.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- **How an REST app works?**
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- What are alternate tools to build back-ends?

---

# How an REST app works? - HTTP protocol

- REST is usually implemented over HTTP protocol
- Having said that REST itself is independent of any particular network protocol

---

# How an REST app works?

- URLs to represent objects
- HTTP Verbs
- Data format of HTTP response
- Response codes
- Cache control

---

# How an REST app works?

## URLs to represent resources

sample URL to access a backend resource

```http://example.com/resource```

To pass some value to backend

```http://example.com/resource?parameter=value```

To pass more than one value to backend

```http://example.com/update_widget?parameter1=value1&parameter2=value2```

---

# How an REST app works?

## HTTP Verbs

- GET - to read the resource
- PUT - modify the resource
- POST - create the resource
- DELETE - delete the resource

---

# How an REST app works?

## Example of usage of HTTP verbs

- If we wanted to view all the resources in the server, the URL would look like this:
	
	``` GET http://example.com/resources ```

- Create a new resource by posting the data:
  	
  	``` POST http://example.com/resources?new_resourceid = value ```

- To view a single resource we "get" it by specifying that resource's id:
  	
  	```GET http://example.com/resources/resourceid```

---
# How an REST app works?

## Example of usage of HTTP verbs


- Update newly created resource by "putting" the new data:

	```PUT http://example.com/resources/resourceid?parameter = new value```

- Delete that resource:

	```DELETE http://example.com/resources/resourceid```

---

# How an REST app works?

## Data format of HTTP response - JSON

Sample JSON object of response object

	!json 

	{
	    "parameter":"value",
	    "parameter":number,
	    "nested parameter": {
	        "parameter":"value",
	    }
	 }

---

# How an REST app works?

## Response codes

Here's a list of the most important status codes:

* 2xx = Success
	- 200 - OK (the default)
	- 201 - Created
	- 202 - Accepted (often used for delete requests)
* 3xx = Redirect
---

# How an REST app works?

## Response codes

* 4xx = User error
	- 400 - Bad Request (generic user error/bad data)
	- 401 - Unauthorized (this area requires you to log in)
	- 404 - Not Found (bad URL)
	- 405 - Method Not Allowed (wrong HTTP method)
	- 409 - Conflict (i.e. trying to create the same resource with a PUT request)
* 5xx = Server error

---

# How an REST app works?

## Cache control

In HTTP header, an REST server can specify weather to store the response in the cache and for how long

```
Cache-Control: no-cache
Cache-Control: max-age=<seconds>
```

---

# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- **Lets build a simple application - Chat app**
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- What are alternate tools to build backend?

---

# Lets build a simple application - Chat app

Requirements for our chat app

- client can ***send messages*** with message_id to server
- client can ***see all messages*** and message_ids
- client can ***modify an existing message*** using its message_id
- client can ***delete a message*** using its message_id

<!--
=======
 The app we are building is a  very basic IRC application, if you need a quick introduction on IRC,
its, its a way better and older version of SLACK!

The idea is simple, a basic IRC server with no authentication and a single room.
Multiple clients can talk to the IRC server, each client can post a message as as retrieve all
messages that are posted. Messages are sorted on the server based on the time they are received.

In real IRC, there is the concept of rooms ( equivalent of channels in slack ), however for this
sample program we will only have one default room/channel.
 -->
---

# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- **Two main parts of our app - State and Functionality**
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- What are alternate tools to build backend?

---

# Two main parts of our app - State and Functionality

### State - what we are going to store ?

```Message { message_id, message text, sender client_id }```

### Functionality - what it has to do ?

- Create a new message with a message_id
- Edit an existing message, given its message_id
- See all messages
- Delete an existing message given its message_id
<!-- =======

Many design patterns e.g. MVC ( which Django psudo uses ) seperate state and functionality.

Here, state referes to the data stored by the site/backend. In our example this may include things
like the message.

On the other hand when we talk about functionality, we refer to the actions taken when a client hits
an endpoint.


// TODO include reason as to why this seperation is good -->

---
# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- **What should it remember? - How to store the state?**
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- What are alternate tools to build backend?
---
# What should it remember? - State

For our chat application there are 2 things we need to store:

1. Messages
⋅⋅* Text ( Max 500 chars )
..* Owner ( Must exist )
..* publish date ( Must follow YYYY-MM-DD HH:MM )
2. Profile/User data
..* Name ( Max 50 chars )
..* Email ( Must follow regex `[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+ )
..* Post count ( Integer

There is much more we can add to these, but for now lets start off with this nice simple base

Bellow is a diagram that should help visualize the data:

<center><img src="media/model_class_diagram.png" alt="drawing"/></center>

---

# Functionality

Here are the tasks we are going to allow our server to perform:

1. Create profiles
2. Update profile data
..* Here we only allow the email and name to change
3. Create messages
4. View a single profile given an id
5. View a single message given an id
6. View all messages given an id

---

# Endpionts/URLs

This is important, think of these as function calls!

* address/irc/profiles/<id>?/
* address/irc/chat/<id>?/

We have 5 functions, how can we represent them in 2 URLs?

# Verbs
* address/irc/profiles/<id>?/
..* POST: Create a message
..* GET: View a message or all message is id not specified
* address/irc/chat/<id>?/
..* POST: Ceate a profile
..* GET: Retrieve a profile
..* PUT: Update a profile

---
# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- **Lets implement them in python**
- How to run it? 
- What are alternate tools to build backend?

---

# Creating a django project

If you are going to use Django in your project, I recommend looking at the official Django tutorial
[Django Official Tutorial]

[Django Official Tutorial]: https://docs.djangoproject.com/en/2.1/intro


1. Create a folder: `mkdir -p ~/cpen321/backend`
2. Create a Django project: `django-admin startproject <project name>`
3. `cd` into the project dirrectory `cd ~/cpen321/backend`
4. Create an app withing Django: `./manage.py startapp irc`

This will create the following directory structure:

<center><img src="media/dir-structure.png" alt="drawing"/></center>


## Where and how to store information

When it comes to storage you have several options:

1. SQL Database
2. No-SQL Database
3. Local file based approach
4. etc...

Generally speaking, a lot of backend frameworks support multiple database backends.
You might descredit the use of a file based approach ( "in house db" ) and for a lot of data it
certainly has flaws but think of GIT for a second, it technically has a file based database.

In this tutorial we will be using a built in SQLite databse. However, for your own professional
development, I highly encourage you set up a dedicated database. A lot of jobs will ask for
familiarity with one of them!

Once you have chosen your SQL database of choice you will need to configure the bindings to your
backend.

## Django: Using the database

Using [the django DB binding guide] go ahead and set up the databse..

[the django DB binding guide]: https://docs.djangoproject.com/en/2.1/topics/install/#database-installation

## Basic Models

A model is the way Django uses to represent data as a class, it also acts as an abstraction layer
for you between the framework and the database.

This effectively lets you completely ignore the DB ( You dont have to learn how to write SQL
queries.

Lets begin by the defining the models.

```
class Profile( models.Model ):
    name = models.CharField( max_length=25 )
    post_count = models.IntegerField( default=0 )
    email = models.CharField( max_length=1000 )

class Message( models.Model ):
    owner = models.ForeignKey( Profile, on_delete=models.CASCADE )
    message_text = models.CharField( max_length=10000 )
    pub_date = models.DateTimeField( 'date published' )
```

_Note: We will build on these models as the presentaion progesses!_

## Django: Registering the models and migrating

Turns out django generates all of the SQL for you, infact in order to set up the data base all you
have to run is:

`./manage.py makemigrations`

`./manage.py migrate`

This generates and runs the SQL commands that create and modify the tables based on what you have

---
# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- **What should it do? - How to implement functionality?**
- Final application
- How to run it? 
- What are alternate tools to build backend?

---
# What should it do? - How to implement functionality?

- **create a new message with message_id**

```POST http://www.messageapp.ca/message?message_id = "value"&message="text"&client_id="id"```

- **edit an existing message with message_id**

```PUT http://www.messageapp.ca/message?message_id = "value"&message="text```

---
# What should it do? - How to implement functionality?

- **see all messages**

```GET http://www.messageapp.ca/message```

- **delete an existing message with message_id**

```DELETE http://www.messageapp.ca/message?message_id = "value"```

---
# Lets implement them in python

<!-- The app we are building is a  very basic IRC application, if you need a quick introduction on IRC,
its, its a way better and older version of SLACK!

The idea is simple, a basic IRC server with no authentication and a single room.
Multiple clients can talk to the IRC server, each client can post a message as as retrieve all
messages that are posted. Messages are sorted on the server based on the time they are received.

In real IRC, there is the concept of rooms ( equivalent of channels in slack ), however for this
sample program we will only have one default room/channel. -->


<!-- ## Frameworks:
There are many frameworks we can use to create convenience:
    * Django
    * Flask
    * Ruby On Rails
    * ASP.net
    * etc...

For the most part most of these frameworks only differ in syntax, language, and design methodology
( how they expect you to do stuff ). The underlying principles and concepts always carry over!
 -->

There are many python frameworks (like Django,Flask ...) etc that can help in building REST backends

In this course we will be using Django. Thus this tutorial will be both a general backend and a
mini-django tutorial.

If you are going to use Django in your project, I recommend looking at the official Django tutorial
[Django Official Tutorial]

// TODO Reason

[Django Official Tutorial] -->


---
# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- **How to run it? **
- What are alternate tools to build backend?

---
# How to run it? - locally



---
# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? 
- **What are alternate tools to build backend?**
---
# What are alternate tools to build backend?
