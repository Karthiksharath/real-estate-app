from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProfileModel
from .serializers import ProfileSerializer, UpdateProfileSerializer
from .renderers import ProfileJsonRenderer
from .exceptions import NotYourProfile, ProfileNotFound



class AgentListView(generics.ListAPIView):

  permission_classes = [permissions.IsAuthenticated]
  queryset = ProfileModel.objects.filter(is_agent=True)
  serializer_class = ProfileSerializer


class TopAgentListView(generics.ListAPIView):

  permission_classes = [permissions.IsAuthenticated]
  queryset = ProfileModel.objects.filter(top_agent=True)
  serializer_class = ProfileSerializer


class GetProfileView(APIView):

  permission_classes =[permissions.IsAuthenticated]
  renderer_classes = [ProfileJsonRenderer]

  def get(self, request):

    user = self.request.user
    user_profile = ProfileModel.objects.get(user=user)

    serializer = ProfileSerializer(user_profile, context={'request':request})

    return Response(serializer.data, status=status.HTTP_200_OK)
  

class UpdateProfile(APIView):

  permission_classes =[permissions.IsAuthenticated]
  renderer_classes = [ProfileJsonRenderer]

  def patch(self,request,username):

    try:
      ProfileModel.objects.get(user__username=username)
    except ProfileModel.DoesNotExist:
      return ProfileNotFound

    user_name = request.user.username
    if user_name != username:
        raise NotYourProfile
    

    data = request.data
    serializer = UpdateProfileSerializer(instance=request.user.profile, data=data, partial=True)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
    



      


