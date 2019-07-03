import sqlite3

conn=sqlite3.connect('db.sqlite3')
c = conn.cursor()


datas=c.execute("SELECT 账号编号, 石头数量,等级,宠物,更新时间,是否上传 FROM pad_huancun")

for data in datas:
    print(data[0],data[1],data[2],data[3],data[4],data[5])

    # break



conn.close()
c.close()