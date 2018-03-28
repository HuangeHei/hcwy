from django.db import models
from project.models import Projects

# Create your models here.



class UserType(models.Model):

    type_name = models.CharField(max_length=1024,default='保洁')
    type_desc = models.CharField(max_length=1024,null=True,blank=True)

    def __str__(self):
        return self.type_name


class UserBaoXian(models.Model):
    '''
        User 是正式员工
    '''

    bx_type = models.CharField(max_length=1024)                  # 用户名称  商业保险/社会保险
    bx_third_party = models.CharField(max_length=1024)           # 我方购买的保险公司
    bx_create = models.DateTimeField(auto_created=True)          # 保险到期时间
    bx_time = models.DateTimeField()                             # 保险有效期
    bx_number = models.CharField(max_length=1024,null=True)      # 保险编号
    bx_img = models.CharField(max_length=1024,null=True)         # 保险照片

    def __str__(self):
        return self.bx_create


class Root(models.Model):

    root_name = models.CharField(max_length=1024)       # 权限名称
    root_type = models.CharField(max_length=1024)       # 权限类型

    def __str__(self):
        return self.root_name


class User(models.Model):
    '''
        User 是正式员工
    '''

    _sex_choice = ((0, "男"), (1, "女"))

    user_name = models.CharField(max_length=1024)              # 用户名称
    user_passwd = models.CharField(max_length=1024,default='123') #用户密码
    user_project = models.ForeignKey(Projects)                 # 用户所属项目
    user_type = models.ForeignKey(UserType)                    # 职位
    user_phone = models.CharField(max_length=1024)             # 手机号码
    user_id_number = models.CharField(max_length=1024)         # 身份证ID
    user_sex = models.BooleanField(choices=_sex_choice, default=0)               # True 男 False 女
    user_id_img_1 = models.CharField(max_length=1024)          # 身份证照片正面
    user_id_img_2 = models.CharField(max_length=1024)          # 身份证照片反面
    user_img = models.CharField(max_length=1024)               # 人员照片
    user_salary = models.IntegerField(default=1250)            # 人员工资/月薪
    user_root = models.ManyToManyField(Root)                   # 人员权限
    user_create = models.DateTimeField(auto_created=True)      # 人员入职时间
    user_baoxian = models.ForeignKey(UserBaoXian,null=True,blank=True)    # 人员保险
    user_display = models.BooleanField(default=True)           # 牵扯到删除
    user_level = models.IntegerField(default=50)               # 人员等级 数字越小，等级越高


    def __str__(self):
        return "%s:%s" % (self.id,self.user_name)

#--------------------------------------------------------------------------------


class AddUser(models.Model):
    '''
        AddUser 是添加员工的申请单,也是添加到用户数据库中唯一的方式
    '''
    _sex_choice = ((0, "男"), (1, "女"))

    user_name = models.CharField(max_length=1024,null=False)        # 用户名称
    user_phone = models.CharField(max_length=1024,null=False)       # 手机号码
    user_id_number = models.CharField(max_length=1024,null=False)   # 身份证ID
    user_type = models.ForeignKey(UserType)                         # 职位
    user_sex = models.BooleanField(choices=_sex_choice,default=0)   # 0 男 1 女
    user_id_img_1 = models.CharField(max_length=1024,null=False)    # 身份证照片正面
    user_id_img_2 = models.CharField(max_length=1024,null=False)    # 身份证照片反面
    user_img = models.CharField(max_length=1024,null=False)         # 人员照片
    user_create = models.DateTimeField(auto_now_add=True)           # 人员申请时间
    user_desc = models.CharField(max_length=102400,null=False)      # 人员履历

    def __str__(self):

        return "%s:%s" % (self.id,self.user_name)


