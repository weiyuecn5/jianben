from tkinter import *

root=Tk()
root.title('智龙查询工具')
root.geometry()
Label(root,text='\n智龙查询工具\n').pack()
fra_1 = Frame(root)#左边
fra_1.pack(side=LEFT)
fra_2 = Frame(root)#右边
fra_2.pack(side=LEFT)
index_1=Entry(fra_1,bd=3,width=10)
index_2=Entry(fra_1,bd=3,width=10)
index_1.grid(row=0,side=LEFT)
index_2.grid(row=1)
text_1=Label(fra_1,text="1编号 2石头 3单宠")
text_1.grid(row=0)

root.mainloop()