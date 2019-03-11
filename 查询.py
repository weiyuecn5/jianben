import sqlite3
from tkinter import *
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
cwsj={}
#宠物ID对照
cwid=c.execute("SELECT * FROM pad_duizhao")
for row in cwid:
    cwsj[row[0]]=[row[1].replace('\n',''),row[2].replace('\n','')]

#定义查询类型:
cxlx=2
dc=0
#只要编号=1 全要=0
'''
1按账号编号查询
2石头数量查询
3单宠查询
4双宠查询
5三宠查询
6四宠查询
7宠物+石头
'''
zhbh='B110'
stsl_1=150
stsl_2=300
cw_1='643'
cw_2='3716'
cw_3='4410'
cw_4='4412'


def get_shuju(row,zybh=0): #传入一组账号数据获取处理后的数据
    if zybh==1:
        return row[0]+'\n'
    else:
        ls_1=''
        ls_2=''
        ls_3=''
        ls_4=''
        ls_5=''
        ls_6=''
        for i in row[4].split(','):
            if len(i)<3 or len(i)>4:
                continue
            else:
                try:
                    if cwsj[i][1]=='75000':
                        ls_1=ls_1+'['+i+cwsj[i][0]+']'
                    elif cwsj[i][1]=='50000':
                        ls_2 = ls_2 + '[' + i + cwsj[i][0] + ']'
                    elif cwsj[i][1] == '25000':
                        ls_3 = ls_3 + '[' + i + cwsj[i][0] + ']'
                    elif cwsj[i][1]=='15000':
                        ls_4 = ls_4 + '[' + i + cwsj[i][0] + ']'
                    elif cwsj[i][1] == '6000':
                        ls_5 = ls_5 + '[' + i + cwsj[i][0] + ']'
                    else:
                        ls_6 = ls_6 + '[' + i + cwsj[i][0] + ']'
                except:
                    ls_6=ls_6+'['+i+']'
        line_1='账号编号:%s\n'%row[0]
        line_2 ='石头数量:%s\n'%row[1]
        line_3 ='账号等级:%s\n'%row[2]
        line_4 ='更新时间:%s\n'%row[3]
        line_5 ='里限定(7w5):\n%s\n里限定(5w):\n%s\n合作钻(2w5):\n%s\n合作钻(1w5):\n%s\n合作钻(6000):\n%s\n其它宠物:\n%s\n\n'%(ls_1,ls_2,ls_3,ls_4,ls_5,ls_6)
        return  line_1+line_2+line_3+line_4+line_5
def get_jg(cxlx,zybh=0):
    try:
        datas = c.execute("SELECT * FROM pad_shujuku")
        back_data=''
        if cxlx==1:
            c.execute("SELECT * FROM pad_shujuku WHERE 账号编号=?",(zhbh,))
            data =c.fetchone()
            print(get_shuju(data,zybh))
            back_data=get_shuju(data,zybh)
        elif cxlx==2:
            for data in datas:
                if data[1]!='':
                    if stsl_1<=int(data[1])<=stsl_2:
                        print(get_shuju(data,zybh))
                        back_data=back_data+get_shuju(data,zybh)
        elif cxlx==3:
            for data in datas:
                if ','+cw_1 in ','+data[4]:
                    print(get_shuju(data,zybh))
                    back_data=back_data+get_shuju(data,zybh)
        elif cxlx==4:
            for data in datas:
                if ','+cw_1 in ','+data[4] and  ','+cw_2 in ','+data[4]:
                    print(get_shuju(data,zybh))
                    back_data=back_data+get_shuju(data,zybh)
        elif cxlx==5:
            for data in datas:
                if ','+cw_1 in ','+data[4] and  ','+cw_2 in ','+data[4] and  ','+cw_3 in ','+data[4]:
                    print(get_shuju(data,zybh))
                    back_data=back_data+get_shuju(data,zybh)
        elif cxlx==6:
            for data in datas:
                if ','+cw_1 in ','+data[4] and  ','+cw_2 in ','+data[4] and  ','+cw_3 in ','+data[4] and  ','+cw_4 in ','+data[4]:
                    print(get_shuju(data,zybh))
                    back_data=back_data+get_shuju(data,zybh)
        elif cxlx==7:
            for data in datas:
                if data[1] != '':
                    if stsl_1<=int(data[1]) and  ','+cw_1 in ','+data[4]:
                        print(get_shuju(data,zybh))
                        back_data=back_data+get_shuju(data,zybh)

        with open('结果.txt','w',encoding='utf-8') as f:
            zs='找到的数据数量为:%s\n'%back_data.count('账号编号')
            f.writelines(zs+back_data)
    except:
        pass

get_jg(cxlx,dc)

