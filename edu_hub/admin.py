from django.db import models
from edu_hub.models import Connection, Member, Message, MessageRecipient, Post
from django.contrib import admin

models = (Member, Message, MessageRecipient, Post, Connection)

for model in models:

    admin.site.register(model)

