"""hc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from index import views as index_v
from user import views as user_v
from check import views as check_v
from attence import views as attence_v


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^out/', index_v.Out.as_view()),
    url(r'^index/', index_v.Index.as_view()),
    url(r'^login/', index_v.Login.as_view()),
    url(r'^upload/', index_v.UploadImg.as_view()),
    url(r'^delupload/', index_v.DelUpload.as_view()),
    url(r'^getprojectsetting/', index_v.GetProjectSetting.as_view()),

    #user

    url(r'^user/add',user_v.AddUser.as_view()),
    url(r'^user/list',user_v.GetUserList.as_view()),
    url(r'^user/check_user/',user_v.GetAddUserCheckList.as_view()),
    url(r'^user/get_add_user_info/',user_v.GetAddUserInfo.as_view()),
    url(r'^user/get_user_info/',user_v.GetUserInfo.as_view()),
    url(r'^user/get_add_user_check/',user_v.GetAddUserCheck.as_view()),


    #check

    url(r'^getchecktype/', check_v.GetProcessType.as_view()),

    # attence

    url(r'^postattence/', attence_v.Attence.as_view()),

]
