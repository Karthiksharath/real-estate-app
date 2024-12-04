from django.db import models
from apps.common.models import CommonModel
from apps.profiles.models import ProfileModel
from REAL_ESTATE.settings.base import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


class RatingModel(CommonModel):

      class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

      rating_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

      agents = models.ForeignKey(ProfileModel, null=True, on_delete=models.SET_NULL,related_name="agent_review",)

      ratings = models.IntegerField(choices=Range.choices, default=0 )

      comments = models.TextField()

      class Meta:
          
          unique_together = ['agents', 'rating_user']

          # to ensure a user can rate a agent only once. 
          # it creates a unique key to check for the combination of these two fields.

      def __str__(self):
          return f'{self.rating_user} rated {self.agents}'







