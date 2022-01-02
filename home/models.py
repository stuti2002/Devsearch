from django.db import models
import uuid
from users.models import Profile


# Create your models here.
class Project(models.Model):
    owner=models.ForeignKey(Profile , null=True ,blank=True ,on_delete=models.SET_NULL)
    Title=models.CharField(max_length=50)
    Desc=models.TextField(null=True ,blank=True)
    Upload_image=models.ImageField(blank=True, null=True ,upload_to='profiles/',default="profiles/image.jpg")
    demo_link=models.CharField(max_length=2000,null=True , blank=True)
    Tags=models.ManyToManyField('Tag', blank=True)
    vote_total=models.IntegerField(default= 0,null=True ,blank=True)
    
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    def __str__(self):  
        return self.Title

class Review(models.Model):
    vote_type =(
        ('like' , 'like'),
        ('dislike', 'dislike')
    )
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True ,blank=True)
    value = models.TextField(null=True ,blank=True ,choices =vote_type)
    
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)   
    def __str__(self):
        return self.value
class Tag(models.Model):
    name=models.CharField(max_length=200)
    
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)

    def __str__(self):
        return self.name
    



