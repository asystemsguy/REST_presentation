# Tutorial for creating RESTful Backends

---

# Agenda

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is REST and why to use it?
- How an REST app works?
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

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

Introduction to create a simple REST backend.

<img src="media/backend.jpg" alt="drawing" style="float:right;width:250px;height:160px;"/>

- What is a REST application and why to use it?
- **How an REST app works?**
- Lets build a simple application - Chat app
- Two main parts of our app - State and Functionality
- What should it remember? - How to store the state?
- What should it do? - How to implement functionality?
- Final application
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

---

# How an REST app works?


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
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

---

# Lets build a simple application - Chat app



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
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

---

# Two main parts of our app - State and Functionality

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
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

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
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

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
- **Final application**
- How to run it? - locally and on cloud?
- What are alternate tools to build backends?

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
- **How to run it? - locally and on cloud?**
- What are alternate tools to build backends?

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
- How to run it? - locally and on cloud?
- **What are alternate tools to build backends?**
