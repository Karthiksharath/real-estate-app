
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

  fisrt_name = serializers.SerializerMethodField()
  last_name = serializers.SerializerMethodField()
  full_name = serializers.SerializerMethodField(source='get_full_name')
  gender = serializers.SerializerMethodField(source = 'ProfileModel.gender')
  phone_number = serializers.SerializerMethodField(source = 'ProfileModel.phone_number')
  profile_photo = serializers.ImageField(source = 'ProfileModel.profile_photo')
  country = CountryField(source="ProfileModel.country")
  city = serializers.CharField(source="ProfileModel.city")
  top_seller = serializers.BooleanField(source="ProfileModel.top_seller")

  class Meta:
      
    model = User
    fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "full_name",
        "gender",
        "phone_number",
        "profile_photo",
        "country",
        "city",
        "top_seller",
    ]


  def get_first_name(self, obj):
        return obj.first_name.title()

  def get_last_name(self, obj):
        return obj.last_name.title()

  def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation



class CreateUserSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        
        model = User

        fields = ["id", "username", "email", "first_name", "last_name", "password"]