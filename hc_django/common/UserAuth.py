from user.models import User,Root
from django.shortcuts import HttpResponse

class UserAuth():

    def __init__(self):
        pass

    @staticmethod
    def is_login(req):   # 是否登录

        if req.session.get('is_login',False) and req.session.get('user_name',False):
            return True
        else:
            return False


    @staticmethod
    def out_login(req):           # 用户登出
        req.session.delete()
        return True

    @staticmethod
    def login(req,user_name):      # 用户登录

       req.session['is_login'] = True
       req.session['user_name'] = user_name
       return True

    @staticmethod
    def get_login(req):   #获取用户登录状态

        if req.session.get('is_login', None):
            if req.session['is_login'] == True:
                retUser = {
                    'is_login': True,
                    'username': req.session['user_name']
                }
                return retUser
            else:
                return False
        else:
            return False


    def auth(root):

        def outer_wrapper(func):
            def wap(*args, **kwargs):

                try:

                    root_obj = Root.objects.get(root_name = root) # 这一步主要怕蠢萌程序员
                    print(root_obj)
                except Exception as E:

                    print('程序内部') #内部报错信息 以后写入到日志系统中
                    return HttpResponse('程序内部发生问题')

                if UserAuth.is_login(args[1]):

                    try:

                        obj = User.objects.get(user_name = args[1].session['user_name'])

                        try:
                            is_ok = obj.user_root.filter(root_name = root_obj.root_name)

                        except Exception as e:

                            return HttpResponse('cc')

                    except Exception as e:

                        return HttpResponse('not,用户不存在')

                    if is_ok:

                        return func(*args, **kwargs) #执行函数

                    else:

                        return HttpResponse('not,无权限')

                else:

                    return HttpResponse('not,没有登录')


            return wap
        return outer_wrapper
