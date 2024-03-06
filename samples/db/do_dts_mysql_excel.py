import pandas as pd
import time
from datetime import datetime
import pymysql
import os
import xlwt
# 定义从MySQL数据库中取数的函数
def Get_Data_From_MySQL():
	db = pymysql.connect(
		host = '127.0.0.1',
		database = "test",
        user = "root",
        password = "1qazXSW@",# 此处password即MySQL数据库密码
        port = 3306,
        charset = 'utf8'
		)
	cursor = db.cursor()
	effect_row = cursor.execute(
        '''SELECT id,name from user LIMIT 100'''
		)
	row_1 = cursor.fetchall()
# 查询结果存储到Excel文件中
	write_in_time = time.strftime('%Y%m%d_%H%M%S')
	workbook = xlwt.Workbook(encoding = 'utf-8')
	booksheet = workbook.add_sheet(write_in_time,cell_overwrite_ok = True)
	for i,field_desc in enumerate(cursor.description):
		booksheet.write(0,i,field_desc[0])
		i +=1
	for i,row in enumerate(row_1):
		for j,col in enumerate(row):
			booksheet.write(i+1,j,col)
	folder_name = os.path.abspath(r'/Users/sheng/Desktop/二手房贷款诈骗/') # Excel文件存储路径
	save_file_way = folder_name + r'//' +str(write_in_time)+ '本地数据库查询结果''.xls'  # Excel文件名
	workbook.save(save_file_way)

while True:
	if datetime.now() < datetime(2023,5,10,23,59,59):  #查询截止时间为2018-5-10 23:59:59
		Get_Data_From_MySQL()
		time.sleep(3) #每隔一个小时查询一次
	else:
		print("已到截止时间，停止取数。")
		break