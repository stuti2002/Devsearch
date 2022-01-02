import builtins
from django.db import models
from django.db.models.fields import UUIDField
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE ,null=True ,blank=True)
    name=models.CharField(max_length=20 ,null=True ,blank= True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro=models.CharField(max_length=50 ,null=True,blank=True)
    profile_image=models.ImageField(blank=True ,null =True , upload_to='profiles/', default="profiles/user-default.png")
    bio=models.TextField(null=True, blank=True)
    social_website=models.CharField(max_length=20 ,blank=True,null=True)
    linkedin_profile=models.CharField(max_length=20,blank=True,null=True)
    github_account=models.CharField(max_length=20,blank=True,null=True)
    youtube_chanel=models.CharField(max_length=20,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 ,unique=True,primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    owner=models.ForeignKey(Profile ,on_delete=models.CASCADE ,null=True ,blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)