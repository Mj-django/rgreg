from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

admin.site.register(models.user)
admin.site.register(models.user_as)
admin.site.register(models.file)
admin.site.register(models.city)
admin.site.register(models.province)
