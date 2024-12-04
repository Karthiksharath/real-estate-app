from django.db import models

from django.contrib.auth import get_user_model
from apps.common.models import CommonModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class ProfileModel(CommonModel):

  GENDER_CHOICES = [ ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ]

  user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
  phone_number = PhoneNumberField(max_length=12, default="+91435533232")
  about_me = models.TextField()   
  license = models.CharField(max_length=20, blank=True, null=True)
  profile_photo = models.ImageField(default="/profile_default.png")
  gender = models.CharField(choices=GENDER_CHOICES,max_length=20)
  country = CountryField(max_length=250,default="INDIA", blank=False, null=False)
  city = models.CharField( max_length=180,default="Nairobi",blank=False,null=False,)
  is_buyer = models.BooleanField(default=False,help_text=("Are you looking to Buy a Property?"),)
  is_seller = models.BooleanField(default=False,help_text=("Are you looking to sell a property?"),)
  is_agent = models.BooleanField(default=False, help_text=("Are you an agent?"))
  top_agent = models.BooleanField( default=False)
  rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
  num_reviews = models.IntegerField(default=0, null=True, blank=True)

  def __str__(self):
        return f"{self.user.username}'s profile"                           
    




