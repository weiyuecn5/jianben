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
#获取各个输入框的数据
def call_back():
    get1=int(intext1.get())
    get2=int(intext2.get())
    get3=intext3.get()
    get4=intext4.get()
    get5=intext5.get()
    get6=intext6.get()
    get7=intext7.get()
    return get1,get2,get3,get4,get5,get6,get
cxlx=call_back()[0]
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
def call_back():
    get_jg(cxlx,dc)

root=Tk()
root.title('智龙查询工具')
root.geometry()
fm1=Frame(root)
Label(fm1,text='\n智龙查询工具\n',font='50').pack()
fm1.pack(side=TOP)

fm2=Frame(root)
fm2.pack(side=TOP)
intext1 = Entry(fm2,bd=3,width=10)
intext2 = Entry(fm2,bd=3,width=10)
intext3 = Entry(fm2,bd=3,width=10)
intext4 = Entry(fm2,bd=3,width=10)
intext5 = Entry(fm2,bd=3,width=10)
intext6 = Entry(fm2,bd=3,width=10)
intext7 = Entry(fm2,bd=3,width=10)
intext1.insert(END,'1')
intext2.insert(END,'0')
intext3.insert(END,'100')
intext4.insert(END,'200')
intext5.insert(END,'643')
intext6.insert(END,'3930')
intext7.insert(END,'643')
lab_1=Label(fm2,text = '1编号2石头3单宠4双宠5三宠6四宠7宠物+石头')
lab_2=Label(fm2,text = '只要编号1')
lab_3=Label(fm2,text = '账号编号 最小石头 宠物编号1')
lab_4=Label(fm2,text = '最大石头 宠物编号2')
lab_5=Label(fm2,text = '宠物编号3')
lab_6=Label(fm2,text = '宠物编号4')
lab_7=Label(fm2,text = '宠物+石头的宠物编号')
intext1.grid(row=0,column=1)
intext2.grid(row=1,column=1)
intext3.grid(row=2,column=1)
intext4.grid(row=3,column=1)
intext5.grid(row=4,column=1)
intext6.grid(row=5,column=1)
intext7.grid(row=6,column=1)
lab_1.grid(row=0,column=2)
lab_2.grid(row=1,column=2)
lab_3.grid(row=2,column=2)
lab_4.grid(row=3,column=2)
lab_5.grid(row=4,column=2)
lab_6.grid(row=5,column=2)
lab_7.grid(row=6,column=2)
bt1=Button(fm2,bd=3,command=call_back,text='开始查询',width=10)
bt2=Button(fm2,bd=3,command=root.quit,text='退出',width=10)
bt1.grid(row=7,column=1)
bt2.grid(row=7,column=2)
fm3=Frame(root)
fm3.pack(side=TOP)
lab_8=Label(fm3,text = '\n查询结果\n',font="50").pack()
out_text=Text(fm3)
out_text.pack()
root.mainloop()

