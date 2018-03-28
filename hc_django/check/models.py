from django.db import models
from user.models import User
import json


# Create your models here.


class ProcessType(models.Model):

    process_name = models.CharField(max_length=10240)
    process_type = models.CharField(max_length=10240)
    'process_type   一个可以loads的值'
    def __str__(self):
        return self.process_type


class CheckType(models.Model):

    type_name = models.CharField(max_length=10240,null=False,blank=False)    # 审核类型名称

    def __str__(self):
        return self.type_name

class CheckStatus(models.Model):

    check_status = models.CharField(max_length=1024)                         # 审核状态

    def __str__(self):
        return self.check_status


class Checks(models.Model):
    '''
        重要：审核的流程存放
    '''
    check_type = models.ForeignKey(CheckType)                                           # 审核类型
    check_info = models.IntegerField(blank=False,null=False)                            # 审核顺序 越大优先级越大
    check_status = models.ForeignKey(CheckStatus,default=1)                             # 审核结果 0 未读 1 同意 2 不同意
    check_id  = models.CharField(max_length=1024)                                       # 审核关键字 ID
    check_note = models.CharField(max_length=102400)                                    # note
    check_user = models.ForeignKey(User)                                             # 审核人

    def __str__(self):
        return "%s:%s" % (self.id, self.check_type)



