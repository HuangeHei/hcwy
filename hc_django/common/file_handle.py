import os
import sys
from shutil import copy

def remove_file(path,filelist):

    for file in filelist:
        try:
            os.remove(os.path.join(path, file))
            print('删除成功')
        except FileNotFoundError as e:
            print('找不到文件')
            return False
        except Exception as e:
            print('未知错误',e)
            return False

    return True


def mv_img(_from,_to,filelist):
    '''
    list - mv file
    :param path:  temp dir path
    :param filelist: file_name_list
    :return: true and false
    '''

    for file in filelist:
        try:

            copy(os.path.join(_from, file),os.path.join(_to, file))

        except FileNotFoundError as e:
            print('找不到文件',e)
            return False
        '''except Exception as e:
            print('未知错误',e)
            return False'''

    if remove_file(_from,filelist):
        return True
    else:
        return False