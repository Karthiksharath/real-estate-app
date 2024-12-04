from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):

  status_code = 404
  default_detail = "profile not found."

class NotYourProfile(APIException):

  status_code = 404
  default_detail = "the profile you are trying to access is not your profile."

