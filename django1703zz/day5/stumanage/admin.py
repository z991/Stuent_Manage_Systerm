from django.contrib import admin
from stumanage import models
# Register your models here.
admin.site.register(models.Student)

admin.site.register(models.Class)
admin.site.register(models.UserProfile)