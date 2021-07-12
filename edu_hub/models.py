from django.db import models
# from django.conf import settings
from edu_hub_project.settings import AUTH_USER_MODEL


class Connection(models.Model):
    # connection_member_id = models.ManyToManyField(Member, on_delete=models.CASCADE , null = True, blank = True)
    connection_member_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='connection_member_id', null=True, blank=True)
    member_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member_id', null=True, blank=True)
    connection_date = models.DateTimeField()

class Message(models.Model):
    creator_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name= "creator_id", null=True, blank=True)

    recipient_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name= "recipient_id", null=True, blank=True)
    create_date = models.DateTimeField()
    message_body = models.TextField()

class Post(models.Model):
    create_date = models.DateTimeField()
    post_body = models.TextField()
    creator_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)