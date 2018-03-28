from django.contrib import admin

# Register your models here.



from user import models
# Register your models here.


admin.site.register(models.AddUser)
admin.site.register(models.Root)
admin.site.register(models.UserBaoXian)
admin.site.register(models.User)
admin.site.register(models.UserType)



