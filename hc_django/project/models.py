from django.db import models

# Create your models here.

class ProjectType(models.Model):

    type_name = models.CharField(max_length=1024) # Type Name
    type_desc = models.CharField(max_length=1024) # Type 简介

    def __str__(self):
        return self.type_name

class Projects(models.Model):

    project_name = models.CharField(max_length=1024)   # 项目名称
    project_type = models.ForeignKey(ProjectType)      # 项目类型

    def __str__(self):
        return self.project_name
