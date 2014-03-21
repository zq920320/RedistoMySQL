#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import os
reload(sys)

c_path = os.getcwd()
base_path=c_path[:c_path.rfind("RedistoMySQL")]
sys.path.append(base_path)

from RedistoMySQL.src.dao import redisdao
from RedistoMySQL.src.dao import mysqldao
mysql_exist_app_num=1
# while True:
# 	app_num=redisdao.get_app_num()
# 	print app_num
# 	app_infos=redisdao.get_app_info(mysql_exist_app_num,app_num)
#	mysqldao.insert_app_info(app_infos)
# 	mysql_exist_app_num=app_num

def redistomysql(app_total=10):
	
	app_num=redisdao.get_app_num()
	print app_num
	app_infos=redisdao.get_app_info_bycategory(1,100,app_total)
	#app_infos=redisdao.get_app_info_bydownload(1,100)

	mysqldao.insert_app_info(app_infos)


if __name__ == "__main__":
	if len(sys.argv)>1:
		app_total=sys.argv[1]
		
		redistomysql(app_total)
	else:
	
		redistomysql()