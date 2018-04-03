from django.db import models
from user.models import User
# Create your models here.


class Attence(models.Model):

    user_name = models.ForeignKey(User)  #签到用户
    date = models.DateTimeField(auto_created = True) #签到时间
    local = models.CharField(max_length=1024) # 签到地点
    grid = models.CharField(max_length=1024) # 签到坐标
    ip = models.CharField(max_length=1024,null=True,blank=True)#签到ip

