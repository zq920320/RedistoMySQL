#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import os
import redis
import time
import MySQLdb

'''
	#REDIS配置地址
	*	host: 填写Redis服务器名称或者IP
	*	password: 添加Redis服务器的密码，默认为空
	*	port: 服务器端口，默认为6379
	*	db: redis中配置的数据库编号，默认为0
'''
REDIS = {
    'host':'10.0.1.202',
#	'host': 'localhost',
    'password':'',
    'port':6379,
    'db':0
}

'''
	#Mysql配置地址
	*	host: 填写MySQL服务器名称或者IP
	*	user：填写MySQL用户名
	*	password: 添加MySQL服务器的密码
	*	port: 服务器端口，默认为3306
	*	db: MySQL中配置的数据库编号，默认为test
	*	charset：MySQl数据库用UTF-8
'''
MySQL={
	'host':'localhost',
	'password':'123456',
	'user':'root',
	'db':'test',
	'charset':'utf8',
	'port':3306
}
'''
	strat_app_id应用开始id号
	end_app_id应用结束id号
	app_total要获取的应用总数，默认300
'''


apps_total=20



#向mysql添加数据，app_info是list类型
def insert_app_info(app_infos):
	conn = MySQLdb.connect(host=MySQL['host'],user=MySQL['user'],passwd=MySQL['password'],db=MySQL['db'],port=MySQL['port'],charset=MySQL['charset'])
	cur=conn.cursor()
	sql = "INSERT INTO mdm_disapp_appinfo (app_version, app_name, app_package, app_icon, app_size, app_type, app_from, app_url, app_desc,platform, create_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.executemany(sql,app_infos)
	conn.commit()
	cur.close()
	conn.close()
	return True





pool = redis.ConnectionPool(host=REDIS['host'], password=REDIS['password'], port=REDIS['port'], db=REDIS['db'])
redis_client = redis.Redis(connection_pool=pool)
#通过category获取app信息，传入起始和终止数，返回一个list
def get_app_info_bycategory(app_total):
    app_infos=[]
    app_lists = redis_client.lrange('app::mostpopular',1,redis_client.llen('app::mostpopular'))
    for app_list in app_lists:
        app_list=eval(app_list)
        app_id = redis_client.hget('app::index', app_list[0])
        app=eval(redis_client.lindex('app::data',app_id))
        #获取app分类
        app_type=app_list[1]
        #app名称
        app_name = app['app_name'].encode('utf8', 'ignore')
        #获取app的package_name
        app_package = app['package_name'].encode('utf8', 'ignore')
        #获取app详细信息type=list
        app_details = app['app_detail']
        #获取第一个详细信息type=dict
        app_detail = app_details[0]
        #获取app_version
        app_version = app_detail['version'].encode('utf8', 'ignore')
        #获取app_platform
        platform = 'Android'
        #获取apk_url
        app_url = app_detail['apk_url'].encode('utf8', 'ignore')
        #获取cover
        app_icon = app_detail['cover'].encode('utf8', 'ignore')
        #获取app_size
        app_size = '0'
        #获取app_from
        app_from = app_detail['platform'].encode('utf8', 'ignore')
        #获取app_desc
        app_desc = 'null'
        #获取download_times
        app_download_times=app_detail['download_times'].encode('utf8', 'ignore')
        #获取cover
        cover=app_detail['cover']
        #获取creat_time
        # create_time = app1_detail['last_update'].encode('utf8', 'ignore')
        create_time = '2014-3-14'
        #Mysql数据库
        app_info=[app_version,app_name,app_package,app_icon,app_size,app_type,app_from,app_url,app_desc,platform,create_time]
        
        app_infos.append(app_info)
        #下载app_icon_file
        #CommonUtil.download_icon(cover,app_name)
    

    
    return app_infos

#数据迁移
def redistomysql(app_total=apps_total):
	app_infos=get_app_info_bycategory(app_total)
	print len(app_infos)
	insert_app_info(app_infos)





if __name__ == "__main__":
	print "start"
	start_time = time.time()
	if len(sys.argv)>1:
		app_total=sys.argv[1]
		
		redistomysql(int(app_total))
	else:
	
		redistomysql()
	end_time = time.time()
	print "consume time: %s secs" %(end_time - start_time)