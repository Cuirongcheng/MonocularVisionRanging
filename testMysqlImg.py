import pymysql

# def save_myysql():
fp = open("./imgs/11.png", 'rb')
img = fp.read()
fp.close()
print("创建连接")
# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='monoculardata',
                       charset='utf8', use_unicode=True, )
# 创建游标
cursor = conn.cursor()
print("创建游标")
# 注意使用Binary()函数来指定存储的是二进制
#cursor.execute("INSERT INTO zhihu_image SET touxiang_data= %s" % pymysql.Binary(img))
i=2
sql = 'Insert into images (id,image) values(%d'%i +',binary%s);'
cursor.execute(sql,img)

# 提交，不然无法保存新建或者修改的数据
conn.commit()
print("提交")
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
print('successful!!')
