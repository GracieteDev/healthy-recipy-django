from django.db import models
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """Profile model"""

    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    image = CloudinaryField('image', default='https://res.cloudinary.com/your-cloud-name/image/upload/v1621234567/default.jpg')
    bio = SummernoteTextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)