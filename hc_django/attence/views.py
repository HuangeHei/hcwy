from django.shortcuts import render,HttpResponse
from django.views import View
from common.UserAuth import UserAuth
# Create your views here.


class GetUserAttence(View):
    def get(self,request):
        pass
    def post(self,request):
        pass

class Attence(View):
    def get(self,request):
        return HttpResponse('ok')

    def post(self,request):
        print(request.POST)
        return HttpResponse('ok')


