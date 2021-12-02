import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    shortIntro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/',
                              default='profiles/user-default.png',
                              null=True, blank=True)
    socialGithub = models.CharField(max_length=200, null=True, blank=True)
    socialtwitter = models.CharField(max_length=200, null=True, blank=True)
    sociallinkedin = models.CharField(max_length=200, null=True, blank=True)
    socialYoutube = models.CharField(max_length=200, null=True, blank=True)
    socialWebsite = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
