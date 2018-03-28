from django.contrib import admin
from check import models
# Register your models here.

admin.site.register(models.CheckType)
admin.site.register(models.CheckStatus)
admin.site.register(models.Checks)
admin.site.register(models.ProcessType)



