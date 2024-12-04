
from django.urls import path

from apps.profiles import views


urlpatterns = [

  path("user_profile/", views.GetProfileView.as_view(), name="get_profile"),
  path("update/<str:username>/", views.UpdateProfile.as_view(), name="update_profile"),
  path("agents/all/", views.AgentListView.as_view(), name="all-agents"),
  path("top-agents/all/", views.TopAgentListView.as_view(), name="top-agents"),
]