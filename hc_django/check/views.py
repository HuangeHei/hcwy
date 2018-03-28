from django.shortcuts import render,HttpResponse
from django.core import serializers
from django.views import View
from check.models import ProcessType
from common.UserAuth import UserAuth
import json
# Create your views here.


class GetProcessType(View):

    @UserAuth.auth('获取审核流程')
    def get(self,request):
        ret_list = serializers.serialize('json',ProcessType.objects.all())
        return HttpResponse(ret_list)


    def post(self,request):

        return HttpResponse('not post')