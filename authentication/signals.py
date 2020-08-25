# The primary function of this file is to help save user details

# INSTIGATE A SIGNAL AFTER AN OBJECT IS SAVED
from django.db.models.signals import post_save 
# IMPORT USER MODEL TO SEND THE SIGNAL
from django.contrib.auth.models import User
# IMPORT THE RECER OF THE SIGNAL
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # This is a decoratorto save each user
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
