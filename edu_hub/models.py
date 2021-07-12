from django.db import models
from django.contrib.auth import get_user_model


class Member(models.Model):
    member_type = [('EDUCATOR', 'educator'), ('ORGANIZATION',
                                              'organization'), ('STUDENT', 'student')]
    gender_options = [('M', 'Male'), ('F', 'Female')]
    cities_options = [('AMMAN', 'Amman'), ('ZARQA', 'Zarqa'), ('IRBID', 'Irbid'), ('MAFRAQ', 'Mafraq'), ('SALT', 'Salt'), ('MADABA', 'Madaba'),
                      ('AQABA', 'Aqaba'), ('MA`AN', 'Ma`an'), ('JARASH', 'Jarash'), ('AJLUN', 'Ajlun'), ('KARAK', 'Karak'), ('TAFILAH', 'Tafilah')]

    local = models.BooleanField(default="False")
    city = models.CharField(
        max_length=255, choices=cities_options, default="NULL")

    member = models.CharField(
        max_length=255, choices=member_type, default="NULL")

    first_name = models.CharField(max_length=255, default="NULL")
    last_name = models.CharField(max_length=255, default="NULL")

    organization_name = models.CharField(max_length=255, default="NULL")

    gender = models.CharField(
        max_length=1, choices=gender_options, default="NULL")
    birth_date = models.DateTimeField()

    password = models.CharField(max_length=255, default="NULL")
    email = models.EmailField(default="NULL")

    mobile_number = models.IntegerField(default="NULL")

    specialization = models.CharField(max_length=255, default="NULL")
    interests = models.TextField(default="NULL")
    biography = models.TextField(default="NULL")
    current_organization = models.CharField(max_length=255, default="NULL")

    organization_summary = models.TextField(default="NULL")

    freelancer = models.BooleanField(default="NULL")
    hourly_tutoring_rate = models.IntegerField(default="NULL")

    services = models.TextField(default="NULL")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.first_name


class Connection(models.Model):
    # connection_member_id = models.ManyToManyField(Member, on_delete=models.CASCADE , null = True, blank = True)
    connection_member_id = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='connection_member_id', null=True, blank=True)
    member_id = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='member_id', null=True, blank=True)
    connection_date = models.DateTimeField()

class Message(models.Model):
    create_date = models.DateTimeField()
    message_body = models.TextField()
    creator_id = models.ForeignKey(Member, on_delete=models.CASCADE,related_name= "creator_id", null=True, blank=True)

    recipient_id = models.ForeignKey(Member, on_delete=models.CASCADE,related_name= "recipient_id", null=True, blank=True)

class Post(models.Model):
    create_date = models.DateTimeField()
    post_body = models.TextField()
    creator_id = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=True, blank=True)
