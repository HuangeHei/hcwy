from django.shortcuts import render,HttpResponse
from django.views import View
from django.core import serializers
from common.UserAuth import UserAuth
from user import models
from check import models as check_m
from user.manager import AddUserManager,UserManager
from check.manager import ChecksManager


# Create your views here.

class GetUserList(View):
    @UserAuth.auth('获取人员列表')
    def get(self, request):

        return HttpResponse(UserManager.to_json())

    def post(self, request):
        pass



class GetUserInfo(View):


    def get(self, request):

        return HttpResponse(UserManager.to_json(user_id = request.GET['user_id']))

    def post(self, request):

        pass

class GetAddUserCheckList(View):

    @UserAuth.auth('获取添加人员审核列表')
    def get(self, request):

        return HttpResponse(AddUserManager.to_json())

    def post(self, request):
        pass

class  GetAddUserInfo(View):

    def get(self,request):
        ret = AddUserManager.to_json(add_user_id=request.GET['add_user_id'])
        return HttpResponse(ret)
    def post(self,request):

        pass


class  GetAddUserCheck(View):

    def get(self,request):
        ret = ChecksManager.to_json(add_user_id=request.GET['add_user_id'])
        return HttpResponse(ret)
    def post(self,request):

        pass


class AddUser(View):

    @UserAuth.auth('添加人员')
    def get(self, request):

        ret_list = serializers.serialize('json',models.UserType.objects.all())
        return HttpResponse(ret_list)

    @UserAuth.auth('添加人员')
    def post(self, request):

        data = request.POST

        objects = AddUserManager.add_user(request.POST)

        if objects:
            return HttpResponse('ok')
        else:
            return HttpResponse('not')


class DelUser(View):

    def get(self, request):

        pass

    def post(self, request):
        pass
