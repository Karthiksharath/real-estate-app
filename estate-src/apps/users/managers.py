from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):

  # def verify_email(self, email):
  #   try:
  #     validate_email(email)
  #   except ValidationError:
  #     raise ValueError(_('provide valid email address'))

  def create_user(self,username, email, password, first_name, last_name, **extra_fields):

    if not username :
      raise ValueError(_('User must submit username'))
    if not password :
      raise ValueError(_('User must submit password'))
    if not first_name :
      raise ValueError(_('User must submit first name'))
    if not last_name :
      raise ValueError(_('User must submit last name'))

    if email:
      email = self.normalize_email(email)
      # self.verify_email(email)
    
    else:
      return ValidationError(_('user must provide an valid email'))


    # USER INSTACE CREATION

    user = self.model(
      username=username,
      first_name=first_name,
      last_name=last_name,
      email=email,
      **extra_fields
    )

    user.set_password(password)

    # is_staff and is_superuser fields are set to False by default unless explicitly provided in the extra_fields.
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)


    user.save(using=self._db)
    return user


  def create_superuser(
        self, username, first_name, last_name, email, password, **extra_fields
    ):

    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_superuser',True)
    extra_fields.setdefault('is_active',True)

    if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))

    if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))

    if not password:
            raise ValueError(_("Superusers must include a password"))

    if email:
      email = self.normalize_email(email)
      # self.verify_email(email)

    else:
      return ValueError(_('email required'))

    user = self.create_user(
      username, first_name, last_name, email, password, **extra_fields
    )

    user.save(using=self._db)

    return user



   

    

    

