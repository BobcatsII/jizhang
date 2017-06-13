#-*- coding:utf-8 -*-

import easygui as eg
import os
import sys
sys.path.append(os.getcwd())
import dumporload_data as dl
import datafileexist as df
import inputpurdata as ipd
import outputsaldata as opd

try:
    os.mkdir(os.getcwd() + '\\data')
except:
    None
finally:
    eg.msgbox('欢迎使用记账小本本！^_^',title='记账本',ok_button='开始记录')
    while 1:
        choices=['录入数据','查询数据','退出']
        msg=eg.buttonbox(msg = '请选择您要操作的功能，按Cancel退出系统！',image='choice.gif',title='功能选项',choices=choices)
        if msg=='录入数据':
            button=eg.buttonbox(msg='请选择录入类型',choices=('收入明细录入','支出明细录入','返回上一级'))
            if button == '支出明细录入':
                ipd.inputdata()
            elif button == '收入明细录入':
                opd.outputdata()
            elif button == '返回上一级':
                continue
        elif msg=='查询数据':
            date=eg.integerbox(msg='请输入你要查询的日期，例如：20150101',
                                    lowerbound=11110101,upperbound=99991231)
            if date==None:
                pass
            else:
                check_date=str(date)[:4]+'-'+str(date)[4:6]+'-'+str(date)[6:]
                pur,sal=0,0
                if df.data_file_exists(check_date,modle='pur'):
                    pur=1
                else:
                    pur=0
                if df.data_file_exists(check_date,modle='sal'):
                    sal=1
                else:
                    sal=0
                if pur==1 and sal==1:
                    pur_data=dl.load_data(check_date,modle='pur')
                    sal_data=dl.load_data(check_date,modle='sal')
                    pur_tol_data=dl.count_data(check_date,modle='pur')
                    sal_tol_data=dl.count_data(check_date,modle='sal')
                    eg.textbox(msg=check_date+' 当天的总收入与总支出情况如下：',text='★ 当天的收入明细为：'+ '\n' +'\n'+str(sal_data)+'\n'+'★ 当天的支出明细为：'+ '\n' +'\n'+pur_data+'\n'
                                                +'★ 当天的收入总额为：'+str(sal_tol_data)+'\n'+'★ 当天的支出总额为：'+str(pur_tol_data)+'\n'+'★ 当天的利润为：'+str(sal_tol_data - pur_tol_data))
                elif pur==0 and sal==1:
                    eg.msgbox(msg='系统查询不到当天的支出，只查询到当天的收入情况',title='提示',ok_button='确定')
                    sal_data=dl.load_data(check_date,modle='sal')
                    sal_tol_data = dl.count_data(check_date, modle='sal')
                    eg.textbox(msg=check_date+' 当天的收入情况如下：',text='★ 当天的收入明细为：'+ '\n' +'\n'+str(sal_data)+'\n'+'★ 当天的收入总额： '+str(sal_tol_data))
                elif pur==1 and sal==0:
                    eg.msgbox(msg='系统查询不到当天的收入情况，只查询到当天的支出情况',title='提示',ok_button='确定')
                    pur_data=dl.load_data(check_date,modle='pur')
                    pur_tol_data = dl.count_data(check_date, modle='pur')
                    eg.textbox(msg=check_date+' 当天的支出情况如下：',text='★ 当天的支出明细为：'+ '\n' +'\n'+pur_data+'\n'+'★ 当天的支出总额： '+str(pur_tol_data))
                elif pur==0 and sal==0:
                    eg.msgbox(msg='由于您没有录入当天的数据，系统查询不到当天的收入与支出情况！',title='提示',ok_button='确定')
        elif msg == '退出':
            eg.msgbox('感谢您的使用！Bye', title='记账本', ok_button='欢迎您再次使用！')
            break
        elif msg == None:
            break
