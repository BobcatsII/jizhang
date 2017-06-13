#-*- coding:utf-8 -*-
"""录入进货数据模块"""
def outputdata():
    import easygui as eg
    import os
    import sys
    sys.path.append(os.getcwd())
    import dumporload_data as dl
    import today as td

    expenses = ['余额宝','工资','基金','股票','其他']
    kind = eg.buttonbox(msg='请选择收入方式',title='收入方式方式',choices=expenses)
    while 1:
        inc=eg.multenterbox(msg='收入类型：'+kind, fields=['收入金额：'])
        if '' in inc:
            eg.msgbox(msg='您没有输入任何数据！', title='提示', ok_button='返回上一层')
        else:
            inc.insert(0, kind)
            data=tuple(inc)
            dl.memory_data(data,date=td.today(),modle = 'sal')
            eg.textbox(msg='数据保存成功！',title='收入金额', text='本次录入的收入金额为：'+ inc[1] +' 元')
            pop = eg.buttonbox(msg='是否继续录入数据？', title='记账', choices=['是','否'])
            if pop == '是':
                expenses = ['余额宝', '工资', '基金', '股票', '其他']
                kind = eg.buttonbox(msg='请选择收入方式', title='收入方式', choices=expenses)
                continue
            else:
                break
