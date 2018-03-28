from django.shortcuts import render,HttpResponse
from django.views import View
from common.UserAuth import UserAuth
from common.ToJson import tojson
from common.UpLoad import Upload
from common.file_handle import remove_file
from hc_django.settings import STATICFILES_DIRS,UPLOAD_IMG
from index.models import IndexGlobalSetting as Settings
from index.models import SideItem,ChildItem
from django.core import serializers
from user.models import User
from check.models import ProcessType
from common.UserAuth import UserAuth
import json
import os
# Create your views here.

class Out(View):

    def get(self, request):

        return HttpResponse(json.dumps(UserAuth.out_login(request)))

    def post(self,request):

        if UserAuth.out_login(request):

            return HttpResponse('ok')


class DelUpload(View):

    @UserAuth.auth('删除上传图片')
    def get(self,request):
        return HttpResponse('not get')

    @UserAuth.auth('删除上传图片')
    def post(self,request):

        if request.POST.get('del_img_list',False):

            if remove_file(UPLOAD_IMG,request.POST['del_img_list'].split(',')):
                return HttpResponse('ok')
            else:
                return HttpResponse('not')
        else:
            return HttpResponse('not')





class UploadImg(View):

    def get(self,request):
        return HttpResponse('not get')

    @UserAuth.auth('上传图片')
    def post(self,request):

        if UserAuth.is_login(request):
            up_obj = Upload(request.FILES['file'],UPLOAD_IMG) # 创建up_obj 对象
            ret = {}
            ret['name'] = up_obj.upfile_save()
            ret['state'] = 'ok'

            return HttpResponse(json.dumps(ret))
        else:
            return HttpResponse('not')

class Login(View):
    '''
        访问 Login
    '''

    def get(self, request):

        return HttpResponse(json.dumps(UserAuth.get_login(request)))

    def post(self,request):
        try:
            # 不跳异常那么就是查询到了 跳异常拦截直接error
            User.objects.get(user_name=request.POST['username'], user_passwd=request.POST['userpasswd'])
            UserAuth.login(request, request.POST['username'])
            return HttpResponse('ok')

        except Exception as E:

            return HttpResponse('error')

class Out(View):

    def get(self,request):

        return HttpResponse(json.dumps(UserAuth.out_login(request)))

    def post(self,request):

        if UserAuth.out_login(request):

            return HttpResponse('ok')



class Index(View):
    '''
        访问 index
    '''

    @UserAuth.auth('获取首页')
    def get(self,request):

        return HttpResponse(tojson(SideItem.objects.all())) # side 有专用tojson 下次争取吧to json 做好

    def post(self,request):

        return HttpResponse('ok')

class GetProjectSetting(View):
    '''
        获取projects setting
    '''
    def get(self,request):

        return HttpResponse(serializers.serialize("json", Settings.objects.all()))

    def post(self,request):
        pass



