import json
from check.models import Checks,CheckStatus,CheckType
from user.models import User

class ChecksManager():

    @staticmethod
    def to_json(add_user_id=False):

        ret = []

        if add_user_id:
            object = Checks.objects.filter(check_id=add_user_id).order_by("check_info")  # order_by 保证顺序
        else:
            object = Checks.objects.all().order_by("check_info")


        for item in object:
            _temp = {}
            _temp['check_note'] = item.check_note if item.check_note else '无'
            _temp['check_info'] = item.check_info
            _temp['check_type'] = item.check_type.type_name
            _temp['check_status'] = item.check_status.check_status
            _temp['check_status_id'] = item.check_status.id
            _temp['check_id'] = item.check_id
            _temp['check_user'] = item.check_user.user_name
            _temp['check_user_id'] = item.check_user.id

            ret.append(_temp)



        return json.dumps(ret)


    @staticmethod
    def add_checks(process_type, check_id, check_type, check_note="Null"):
        '''
        :param process_type: 流程审核人员类型（可自定义）
        :param check_id: 对应的id
        :param check_type: 检查类型
        :param check_note: note
        :return:
        '''

        item = 1  # 计数器

        for user in json.loads(process_type.process_type):

            try:
                user_obj = User.objects.get(id=user)
                Checks.objects.create(check_id=check_id,
                            check_type = CheckType.objects.get(type_name=check_type),
                            check_info = item,
                            check_status = CheckStatus.objects.get(id=1),  # 默认为 1 未审核
                            check_user = user_obj,
                            )
                item += 1

            except Exception as E:

                print('出现内部错误，从process提取user失败请查看check_models 33行代码,下面是错误信息:', E)

