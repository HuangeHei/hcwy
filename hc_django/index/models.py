from django.db import models

# Create your models here.


class ChildItem(models.Model):
    '''
        index 页面的全局设置数据库
    '''
    Index = models.CharField(max_length=100,null=False)                  # Side Index
    Name =  models.CharField(max_length=1024,default='无名称设置名称')    # Side Name
    To = models.CharField(max_length=1024,null=False)             # to path
    Icon = models.CharField(max_length=1024,default='None')              # Icon


    def __str__(self):
        return  self.Name


class SideItem(models.Model):
    '''
        index 页面的全局设置数据库
    '''
    Index = models.CharField(max_length=100,null=False)                   # Side Index
    Name =  models.CharField(max_length=1024,default='无名称设置名称')     # Side Name
    Child = models.ManyToManyField(ChildItem)                             # Child Item
    Icon = models.CharField(max_length=1024, default='None')              # Icon

    def __str__(self):
        return  self.Name

class IndexGlobalSetting(models.Model):
    '''
        index 页面的全局设置数据库
    '''

    ProjectName =  models.CharField(max_length=1024,default='无名称设置名称')    # 公司名称
    ProjectColor = models.CharField(max_length=1024,default='#409EFF')          # 公司主体颜色
    ProjectIcon = models.CharField(max_length=1024,default='None')              # 公司Icon

    def __str__(self):
        return  self.ProjectName