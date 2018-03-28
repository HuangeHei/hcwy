from django.core import serializers
import json

def to_json_f():
    pass



def tojson(item_list):
    '''
    为sideitem 打造的json方法
    :param item_list:
    :return:
    '''
    ret_list = []
    
    for item in item_list:
        Child = []

        for child  in item.Child.all():
            Child.append(json.loads(serializers.serialize('json', [child]))[0]['fields'])


        item  = json.loads(serializers.serialize('json',[item]))[0]['fields']
        item['Child'] = Child
        ret_list.append(item)

    return json.dumps(ret_list)




