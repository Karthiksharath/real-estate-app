import logging

from django.db.models.signals import  post_save
from django.dispatch import receiver
from apps.profiles.models import ProfileModel

from REAL_ESTATE.settings.base import AUTH_USER_MODEL



logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def user_profile_create(sender, instance, created, **kwargs):
  if created:
    ProfileModel.objects.create(user=instance)

@receiver(post_save,sender=AUTH_USER_MODEL)
def user_profile_save(sender, instance, **kwargs):
  instance.profile.save()
  logger.info('profile created.')


# functions to handle auto creation and saving of user's profile while a user instamce is created.
# used django signals for decoupling


