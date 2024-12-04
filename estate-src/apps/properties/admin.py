from django.contrib import admin

from .models import PropertyModel, PropertyViewsModel


admin.site.register(PropertyModel)
admin.site.register(PropertyViewsModel)
