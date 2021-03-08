from django.db import models
from django.contrib.auth.models import User

# Create your models here.

AUTH_TYPE = [("password", "Password"), ("token", "Token")]
SERVICES = [("JIRA", "Jira")]


class UserCredentials(models.Model):
    service = models.CharField(choices=SERVICES, null=False, blank=False, max_length=20)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=500, null=True, blank=True)
    authentication_type = models.CharField(choices=AUTH_TYPE, null=False, blank=False, max_length=20, default=AUTH_TYPE[0][0])
    end_point = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.end_point


class Projects(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    key = models.CharField(max_length=100, null=False, blank=False)
    project_id = models.BigIntegerField(null=False, blank=False)
    credentials = models.ForeignKey(UserCredentials, on_delete=models.DO_NOTHING, related_name="project_credential")

    def __str__(self):
        return self.name

