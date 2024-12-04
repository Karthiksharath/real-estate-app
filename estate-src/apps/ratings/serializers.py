from rest_framework import serializers

from apps.ratings.models import RatingModel


class RatingSerializer(serializers.ModelSerializer):

  rating_user = serializers.SerializerMethodField( read_only=True)
  agents = serializers.SerializerMethodField( read_only=True)


  class Meta:

    model = RatingModel
    exclude = ['updated_at', 'pkid']

  
  def get_user(self,obj):

    return obj.rating_user.username

  def get_agent(self,obj):

    return obj.agents.user.username


