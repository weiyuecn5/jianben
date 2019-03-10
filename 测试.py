from tkinter import *

import sqlite3
宠物="""
    新宙斯:4836 新白盾:4834 新小雅:4838 美杜莎:4604  舰长:4602
    王神:4600  情人节零龙:4204  回想时女:4195  万圣玩龙:4830
    万圣木时:3994 暗魔女:4649 光魔女:4647 木魔女:4414 水魔女:4412
    火魔女:4410 彩龙:3930 光克:3645 黑莓:642 玩龙:3896-3901
    零龙:3756-3761 岚龙:3657 金雷公:4135 鏖魔:3663 风神:3414
    光龙帝:2942 光废狗:2899 白狗:1950 火龙机:2712 天央:3602
    光克:3645 灵央:3785 暗咖喱:1587 水时女:1673 爱德华:4019
    幽助:4301
    """

def get_v():
    return int(v.get())
def get_k():
    return int(k.get())
def callback():
    # 查询类型 1.石头 2.单宠 3.双宠 4.等级 5.单号详情 6.查询一组 7.三宠
    out_text.delete('0.0','end')
    cxlx = get_v()
    st_1 = intext4.get()   # 查询的最小石头数量
    st_2 = intext5.get()   # 查询的最大石头数量
    dc_1 = intext1.get()  # 查询的第一个宠物
    dc_2 = intext2.get()   # 查询的第二个宠物
    dc_3 = intext3.get()   # 查询的第二个宠物
    zhbh = intext6.get()   # 单查询编号
    bh = get_k()  # 只要编号1



    with open('dic1.txt', 'r', encoding='utf-8') as  fr:
        dic = {}
        for line in fr:
            v = line.strip().split(':')
            dic[v[0]] = v[1]

    conn = sqlite3.connect('PADDB.db')
    c = conn.cursor()

    cursor = c.execute("SELECT 账号编号, 石头数量,状态,时间, 宠物编号  from 账号数据")
    jg = []
    for row in cursor:
        try:
            int(row[1])
            int(row[2])
        except:
            pass
        else:
            if cxlx == 1:  # 查询石头数量
                if int(row[1]) >= int(st_1) and int(row[1]) <= int(st_2):
                    if bh == 1:
                        print("账号编号:", row[0])
                        jg.append(row[0] + '\n')
                    else:

                        print("账号编号:", row[0])
                        print("石头数量:", row[1])
                        print("等级:", row[2])
                        print("更新时间:", row[3])
                        jg.append("账号编号:" + row[0] + '\n')
                        jg.append("石头数量:" + row[1] + '\n')
                        jg.append("等级:" + row[2] + '\n')
                        jg.append("更新时间:" + row[3] + '\n')
                        b = row[4].split(",")
                        while '' in b:
                            b.remove('')
                        b = [x + dic[x] if x in dic else x for x in b]
                        print("宠物编号:", b, "\n")
                        jg.append("宠物编号:" + str(b) + "\n\n")
            elif cxlx == 2:  # 查询单宠
                if dc_1 in row[4]:
                    if bh == 1:
                        print("账号编号:", row[0])
                        jg.append(row[0] + '\n')
                    else:

                        print("账号编号:", row[0])
                        print("石头数量:", row[1])
                        print("等级:", row[2])
                        print("更新时间:", row[3])
                        jg.append("账号编号:" + row[0] + '\n')
                        jg.append("石头数量:" + row[1] + '\n')
                        jg.append("等级:" + row[2] + '\n')
                        jg.append("更新时间:" + row[3] + '\n')
                        b = row[4].split(",")
                        while '' in b:
                            b.remove('')
                        b = [x + dic[x] if x in dic else x for x in b]
                        print("宠物编号:", b, "\n")
                        jg.append("宠物编号:" + str(b) + "\n\n")
            elif cxlx == 3:  # 查询双宠
                if dc_1 in row[4] and dc_2 in row[4]:
                    if bh == 1:
                        print("账号编号:", row[0])
                        jg.append(row[0] + '\n')
                    else:

                        print("账号编号:", row[0])
                        print("石头数量:", row[1])
                        print("等级:", row[2])
                        print("更新时间:", row[3])
                        jg.append("账号编号:" + row[0] + '\n')
                        jg.append("石头数量:" + row[1] + '\n')
                        jg.append("等级:" + row[2] + '\n')
                        jg.append("更新时间:" + row[3] + '\n')
                        b = row[4].split(",")
                        while '' in b:
                            b.remove('')
                        b = [x + dic[x] if x in dic else x for x in b]
                        print("宠物编号:", b, "\n")
                        jg.append("宠物编号:" + str(b) + "\n\n")
            elif cxlx == 4:  # 查询三宠
                if dc_1 in row[4] and dc_2 in row[4] and dc_3 in row[4]:
                    if bh == 1:
                        print("账号编号:", row[0])
                        jg.append(row[0] + '\n')
                    else:

                        print("账号编号:", row[0])
                        print("石头数量:", row[1])
                        print("等级:", row[2])
                        print("更新时间:", row[3])
                        jg.append("账号编号:" + row[0] + '\n')
                        jg.append("石头数量:" + row[1] + '\n')
                        jg.append("等级:" + row[2] + '\n')
                        jg.append("更新时间:" + row[3] + '\n')
                        b = row[4].split(",")
                        while '' in b:
                            b.remove('')
                        b = [x + dic[x] if x in dic else x for x in b]
                        print("宠物编号:", b, "\n")
                        jg.append("宠物编号:" + str(b) + "\n\n")
            elif cxlx == 6:  # 查询单号详情
                if row[0] == zhbh:
                    print("账号编号:", row[0])
                    print("石头数量:", row[1])
                    print("等级:", row[2])
                    print("更新时间:", row[3])
                    jg.append("账号编号:" + row[0] + '\n')
                    jg.append("石头数量:" + row[1] + '\n')
                    jg.append("等级:" + row[2] + '\n')
                    jg.append("更新时间:" + row[3] + '\n')
                    b = row[4].split(",")
                    while '' in b:
                        b.remove('')
                    b = [x + dic[x] if x in dic else x for x in b]
                    print("宠物编号:", b, "\n")
                    jg.append("宠物编号:" + str(b) + "\n\n")
            elif cxlx == 6:  # 查询单号详情
                if zhbh in row[0]:
                    print("账号编号:", row[0])
                    print("石头数量:", row[1])
                    print("等级:", row[2])
                    print("更新时间:", row[3])
                    jg.append("账号编号:" + row[0] + '\n')
                    jg.append("石头数量:" + row[1] + '\n')
                    jg.append("等级:" + row[2] + '\n')
                    jg.append("更新时间:" + row[3] + '\n')
                    b = row[4].split(",")
                    while '' in b:
                        b.remove('')
                    b = [x + dic[x] if x in dic else x for x in b]
                    print("宠物编号:", b, "\n")
                    jg.append("宠物编号:" + str(b) + "\n\n")
    conn.close()
    with open('结果.txt', 'w', encoding='utf-8') as  f:
        f.writelines(jg)
    with open('结果.txt', 'r', encoding='utf-8') as  f:
        out_text.insert('1.0', f.read())




root = Tk()
root.title('查询工具')
root.geometry()
Label(root,text='\n查询工具\n').pack()
fra = Frame(root)
fra_0 = Frame(root)
fra_0.pack()
#上
lxs = [('石头',1),('单宠',2),('双宠',3),('三宠',4),('等级',5),('组别',6)]
v = IntVar() #tkinter专用整型变量
v.set(2) #设置v的值为1，值多少无所谓了,我的理解是第一组写1，第二组写2，一次递增
for lx,num in lxs:
    #variable = v绑定了一个整型变量
    b = Radiobutton(fra_0,text = lx,variable = v,value = num)
    b.pack(side=LEFT)

Label(fra,text='编号1:          编号2:          编号3:                           ').pack()
k = IntVar() #tkinter专用整型变量
k.set(0)
Radiobutton(root,text='只要编号',variable =k,value = 1).pack()
fra_L = Frame(fra)
fra_L.pack(side=TOP)
fra_L_1=Frame(fra_L)
fra_L_1.pack(side=TOP)
Label(fra_L,text='石头1:          石头2:          账号:                             ').pack()
fra_L_2=Frame(fra_L)
fra_L_2.pack(side=TOP)
fra_L_3=Frame(fra_L)
fra_L_3.pack(side=TOP)
fra_L_4=Frame(fra_L)
fra_L_4.pack(side=TOP)
fra_R = Frame(fra)
Label(fra_R,text='查询结果:').pack()
out_text=Text(fra_R)
fra_R.pack(side=TOP)
out_text.pack()
fra.pack()
intext1 = Entry(fra_L_1, text = '编号1',width=10)
intext2 = Entry(fra_L_1, text = '编号2',width=10)
intext3 = Entry(fra_L_1, text = '编号3',width=10)
Button(fra_L_1,text='宠物查询',command=callback).pack(side=RIGHT,padx=10)
intext4 = Entry(fra_L_2, text = '石头1',width=10)
intext5 = Entry(fra_L_2, text = '石头2',width=10)
intext6 = Entry(fra_L_2, text = '账号',width=10)
Button(fra_L_2,text='账号查询',command=callback).pack(side=RIGHT,padx=10)
intext1.pack(side=LEFT)
intext2.pack(side=LEFT)
intext3.pack(side=LEFT)
intext4.pack(side=LEFT)
intext5.pack(side=LEFT)
intext6.pack(side=LEFT)


Button(fra_L,text='退出',command=root.quit).pack(side=RIGHT,padx=5)
Label(root,text=宠物).pack()
root.mainloop()