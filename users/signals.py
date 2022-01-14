from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from users.models import Profile

from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save,sender=Profile)
def profileUpdated(sender,instance,created,**kwargs):
    print("Profile saved")
    print('Instance :',instance)
    print('Created :',created)



def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

@receiver(post_delete,sender=Profile)
def profileDeleted(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    print("profile deleted...")
    print('Instance :',instance)

post_save.connect(createProfile, sender=User)

# post_delete.connect(profileDeleted, sender=Profile)



