#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import os
reload(sys)

c_path = os.getcwd()
base_path=c_path[:c_path.rfind("src")]
sys.path.append(base_path)

from src.dao import redisdao
from src.dao import mysqldao
mysql_exist_app_num=1
# while True:
# 	app_num=redisdao.get_app_num()
# 	print app_num
# 	app_infos=redisdao.get_app_info(mysql_exist_app_num,app_num)
#	mysqldao.insert_app_info(app_infos)
# 	mysql_exist_app_num=app_num


app_num=redisdao.get_app_num()
print app_num
app_infos=redisdao.get_app_info(1,10000)

mysqldao.insert_app_info(app_infos)