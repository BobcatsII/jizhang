#-*- coding:utf-8 -*-
"""录入进货数据模块"""
def inputdata():
    import easygui as eg
    import os
    import sys
    sys.path.append(os.getcwd())
    import dumporload_data as dl
    import today as td

    expenses = ['花呗','白条','现金','银行卡']
    kind = eg.buttonbox(msg='请选择支出方式',title='支出方式',choices=expenses)
    while 1:
        pay_type=eg.buttonbox(msg='支出方式：'+kind+'\n'+'今日日期：'+td.today()+'\n', title="支出类型：", choices=['餐饮','服饰','交通','医疗','家居','其他'])
        pay=eg.multenterbox(msg='支出类型：'+pay_type, fields=['支出金额：'])
        if '' in pay:
            eg.msgbox(msg='您没有输入任何数据！', title='提示', ok_button='返回上一层')
        else:
            pay.insert(0, pay_type)
            data=tuple(pay)
            dl.memory_data(data,date=td.today())
            eg.textbox(msg='数据保存成功！',title='支出金额', text='本次录入的支出金额为： '+ pay[1] +' 元')
            pop = eg.buttonbox(msg='是否继续录入数据？', title='记账', choices=['是','否'])
            if pop == '是':
                expenses = ['花呗', '白条', '现金', '银行卡']
                kind = eg.buttonbox(msg='请选择支出方式', title='支出方式', choices=expenses)
                continue
            else:
                break
