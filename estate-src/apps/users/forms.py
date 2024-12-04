from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserModel


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        
        model = UserModel
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        
        model = UserModel
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


