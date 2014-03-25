#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
reload(sys)
c_path = os.getcwd()
base_path=c_path[:c_path.rfind("RedistoMySQL")]
sys.path.append(base_path)
from RedistoMySQL.config import Config
from RedistoMySQL.src.util import CommonUtil
import MySQLdb

Mysql=Config.MySQL
#向mysql添加数据，app_info是list类型
def insert_app_info(app_infos):
	conn = MySQLdb.connect(host=Mysql['host'],user=Mysql['user'],passwd=Mysql['password'],db=Mysql['db'],port=Mysql['port'],charset=Mysql['charset'])
	cur=conn.cursor()
#	sql = "INSERT INTO mdm_disapp_appinfo (app_version, app_name, app_package, app_icon, app_size, app_type, app_from, app_url, app_desc,platform, create_time) VALUES ('"+app_version+"', '"+app_name+"', '"+app_package+"', '"+app_icon+"', '"+app_size+"','"+app_type+"', '"+app_from+"', '"+app_url+"', '"+app_desc+"','"+platform+"', '"+create_time+"')"
	sql = "INSERT INTO mdm_disapp_appinfo (app_version, app_name, app_package, app_icon, app_size, app_type, app_from, app_url, app_desc,platform, create_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.executemany(sql,app_infos)
	conn.commit()
	cur.close()
	conn.close()
	return True


