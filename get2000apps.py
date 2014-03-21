#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import os
import redis
import time


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
	app_total要获取的应用总数，默认2000
'''


apps_total=2000
level=20








pool = redis.ConnectionPool(host=REDIS['host'], password=REDIS['password'], port=REDIS['port'], db=REDIS['db'])
redis_client = redis.Redis(connection_pool=pool)
#通过category获取app信息，传入起始和终止数，返回一个list
def get_app_info_bycategory(app_total):
    all_app_num=int(redis_client.get('app::amount'))
    app_infos=[]
    for i in range(1):
        part_start_app_num=(all_app_num/100)*(i+1)
        part_end_app_num=(all_app_num/100)*(i+2)
        #app_lists = redis_client.lrange('app::data',35,2000)
        app_lists = redis_client.lrange('app::data',part_start_app_num,part_end_app_num)
        
        for app in app_lists:
            app = eval(app)

            #通过sort对category重新排序，将app_type存成分类数最大的分类+分类数的和，方便在最后的排序
            
            app_type=app['category'].encode('utf8', 'ignore')
            app_type=app_type.split(',')
            app_type.sort(key=lambda x:int(x.split(':')[1]))
            flag=False
            num=0
            for tmp in app_type:
                tmp=int(tmp.split(':')[1])
                num+=tmp
            if num>=level:
                app_type=app_type[0].split(':')[0]+':'+str(num)
                flag=True
            if flag==True:
            

                #app名称
                app_name = app['app_name'].encode('utf8', 'ignore')
                
                #Mysql数据库
                app_info=[app_name,app_type]
                app_infos.append(app_info)
                #下载app_icon_file
                #CommonUtil.download_icon(cover,app_name)
            flag=False
        
        
    if len(app_infos)>=app_total:
        #对app_info排序
        app_infos.sort(key=lambda x:int(x[1].split(':')[1]))
        app_infos=app_infos[-(app_total):]
   
   
    return app_infos


def save_apps(app_infos):
    redis_client.delete('app::mostpopular')
    
    for i in range(len(app_infos)):
        redis_client.rpush('app::mostpopular',i)
        redis_client.lset('app::mostpopular',i,app_infos[i])
        
   

#数据迁移
def save_2000apps(app_total=apps_total):
    app_infos=get_app_info_bycategory(app_total)
    
    save_apps(app_infos)





if __name__ == "__main__":
	print "start"
	start_time = time.time()
	if len(sys.argv)>1:
		app_total=sys.argv[1]
		
		save_2000apps(int(app_total))
	else:
	
		save_2000apps()
	end_time = time.time()
	print "consume time: %s secs" %(end_time - start_time)