from django.db import models
from edu_hub.models import Connection, Member, Message, Post
from django.contrib import admin

models = (Member, Message, Post, Connection)

for model in models:

    admin.site.register(model)

