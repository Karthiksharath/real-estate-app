from django.db import models
import uuid


class CommonModel(models.Model):

  primary_key_id = models.BigAutoField(primary_key=True, editable=False)
  id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True
