from django.db import models
from edu_hub.models import Connection, Member, Message, Chat, Post
from django.contrib import admin

models = (Member, Message, Chat, Post, Connection)

for model in models:

    admin.site.register(model)

