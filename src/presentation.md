# Tutorial for creating RESTful backend

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

## REST backend for a chat app 

Requirements

- client can ***send messages*** with message_id to server
- client can ***see all messages*** and message_ids
- client can ***modify an existing message*** using its message_id
- client can ***delete a message*** using its message_id

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

Lets define an JSON object for our message

	!json 

	{
	    "id":"message id",
	    "message":"text",
	    "client": {
	        "id":"client id",
	    }
	 }

---
# What should it remember? - State

Lets give an URL for our message 

```http://www.messageapp.ca/message```

if we want to send a message id to this URL

```http://www.messageapp.ca/message?message_id = "value"```

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
# Lets implement them in python



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