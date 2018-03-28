from django.contrib import admin
from index import models
# Register your models here.

admin.site.register(models.IndexGlobalSetting)
admin.site.register(models.SideItem)
admin.site.register(models.ChildItem)