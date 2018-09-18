
# Backend basics

## Azure - Demo

Create a resource group called irc
Create a basic server called ircserver
Whitelist port 22, and port 8000 for django
Show them how to get the IP, SSH and apt update  & upgrade the server
Show them SCP

---
# Backend basics

## PostgreSQL - Demo

Create a psql resource as per https://docs.microsoft.com/en-us/azure/postgresql/quickstart-create-server-database-portal
Make sure to tel them about whitelisting the IP address of their local device, and tell them they dont need to do this for
ircserver since its already on MS servers

---
# Implement the chat app in python

## Creating a Django project

IMPORTANT: Talk about the URL routing mechanism through URLS.py

---
# Implement the chat app in python

## Views basics

Demo the diff return types, HttpResponse and JsonResponse as well as error codes ( status= )
Be SURE to show off curl


After show them the models and run ./manage.py makemigrations and ./manage migrate to apply model to DB


Finally walk through the messages and profile views
