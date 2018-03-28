from common.file_handle import mv_img
from check.models import Checks,ProcessType
from check.manager import ChecksManager
from user import models as User
from hc_django.settings import STATICFILES_DIRS,UPLOAD_IMG,USER_IMG

import json

class UserManager():

    @staticmethod
    def to_json(user_id = False):


        ret = []

        if user_id:

            objects = User.User.objects.filter(id = user_id)

        else:

            objects = User.User.objects.all()



        for item in objects:

            _item = {}
            _item['user_id'] = item.id
            _item['user_name'] = item.user_name
            _item['user_id_number'] = item.user_id_number
            _item['user_project'] = item.user_project.project_name
            _item['user_type'] = item.user_type.type_name
            _item['user_phone'] = item.user_phone
            _item['user_sex'] = '女' if item.user_sex else '男'
            _item['user_create'] = item.user_create.strftime("%Y-%m-%d %H:%M:%S")
            _item['user_level'] = item.user_level
            _item['user_img'] = "http://127.0.0.1:8000/static/userimg/%s" % (item.user_img)
            _item['user_id_img'] = ("http://127.0.0.1:8000/static/userimg/%s" % (item.user_id_img_1),
                                    "http://127.0.0.1:8000/static/userimg/%s" % (item.user_id_img_2))

            ret.append(_item)

        return json.dumps(ret)


class AddUserManager():

    @staticmethod
    def add_user(user_info):

        try:
            _user_type = User.UserType.objects.get(id = user_info['user_type'])
            _check_type = ProcessType.objects.get(id = user_info['check_type'])
        except Exception as E:
            print('查找user_type 或 check_type 错误，请检查！')
            return False

        id_img = user_info['id_img'].split(',') # id_img 是身份证正反面，但是是str的列表所以需要切割一下

        try:
            add_user_obj = User.AddUser.objects.create(
                user_name = user_info['user_name'],
                user_phone = user_info['user_phone'],
                user_id_number = user_info['user_id_number'],
                user_sex = 0 if user_info['user_sex'] == "男" else 1,
                user_img = user_info['img'],
                user_id_img_1 = id_img[0],
                user_id_img_2 = id_img[1],
                user_desc = user_info['user_desc'],
                user_type = _user_type,

            )

            ChecksManager.add_checks(_check_type,
                                      add_user_obj.id,
                                      'AddUser'
                                      )


        except Exception as E:

            print('发生错误',E)

            return False

        mv_list = id_img  # 添加数据
        mv_list.append(user_info['img'])# 添加数据

        if mv_img(UPLOAD_IMG,USER_IMG,mv_list):
            return True
        else:
            return False

    @staticmethod
    def to_json(add_user_id = False):

        ret = []

        if add_user_id:
            objects = User.AddUser.objects.filter(id=add_user_id)
        else:
            objects = User.AddUser.objects.all()


        for item in objects:

            _item = {}
            _item['user_id'] = item.id
            _item['user_name'] = item.user_name
            _item['user_id_number'] = item.user_id_number
            _item['user_type'] = item.user_type.type_name
            _item['user_phone'] = item.user_phone
            _item['user_sex'] = '女' if item.user_sex else '男'
            _item['user_create'] = item.user_create.strftime("%Y-%m-%d %H:%M:%S")
            _item['user_img'] = "http://127.0.0.1:8000/static/userimg/%s" % (item.user_img)

            _item['user_id_img'] = ("http://127.0.0.1:8000/static/userimg/%s" % (item.user_id_img_1),
                                    "http://127.0.0.1:8000/static/userimg/%s" % (item.user_id_img_2))

            _item['user_desc'] = item.user_desc
            ret.append(_item)

        return json.dumps(ret)