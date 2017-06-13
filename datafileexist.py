#-*- coding:utf-8 -*-
"""判断相关数据文件是否存在"""
def data_file_exists(date,modle='pur'):
    import os
    if os.path.exists(os.getcwd()+'\\data'+'\\'+modle+date+'.db'):
        return True
    else:
        return False

if __name__=='__main__':
    data_file_exists(date)
