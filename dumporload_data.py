#-*- coding:utf-8 -*-
"""存储以及读取数据"""
def memory_data(data, date, modle = 'pur'):
    import os
    with open(os.getcwd()+'\\data'+'\\'+ modle + date +'.db', 'a') as f:
        data=' '.join(data)
        f.write(data+'\n')

def load_data(date, modle = 'pur'):
    import os
    with open(os.getcwd() + '\\data' + '\\' + modle + date + '.db', 'r') as f:
        lines = f.readlines()
        data = '\n'.join(lines)
    return data


def count_data(date, modle = 'pur'):
    import os
    with open(os.getcwd() + '\\data' + '\\' + modle + date + '.db', 'r') as f:
        lines = f.readlines()

        data = sum([float(item.split()[1]) for item in lines])
    return data

if __name__=='__main__':
    memory_data(data)


if __name__=='__main__':
    count_data(date)
