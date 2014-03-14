#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
reload(sys)

c_path = os.getcwd()
base_path=c_path[:c_path.rfind("src")]
sys.path.append(base_path)
from src.util import RedisUtil

redis_client = RedisUtil.RedisClient()
def get_app_info(startnums,endnums):
    
    app_lists = redis_client.get_items('app::data',startnums,endnums)
    app_infos=[]
    for app1 in app_lists:
        app1 = eval(app1)
        tmps=app1['category'].encode('utf8', 'ignore')
       
        tmps=tmps.split(',')
        flag=False
        for tmp in tmps:
            
            tmp=int(tmp.split(':')[1])
           
            if tmp>=6:
                flag=True
                break
        if flag==True:
        

            #app名称
            app_name = app1['app_name'].encode('utf8', 'ignore')
            app_name = app1['app_name'].encode('utf8', 'ignore')
            #app类型3200:9999,1100:1
            app_type = app1['category'].encode('utf8', 'ignore')
            #获取app的package_name
            app_package = app1['package_name'].encode('utf8', 'ignore')
            #获取app详细信息type=list
            app1_details = app1['app_detail']
            #获取第一个详细信息type=dict
            app1_detail = app1_details[0]
            #获取app_version
            app_version = app1_detail['version'].encode('utf8', 'ignore')
            #获取app_platform
            platform = 'Android'
            #获取apk_url
            app_url = app1_detail['apk_url'].encode('utf8', 'ignore')
            #获取cover
            app_icon = app1_detail['cover'].encode('utf8', 'ignore')
            #获取app_size
            app_size = '0'
            #获取app_from
            app_from = app1_detail['platform'].encode('utf8', 'ignore')
            #获取app_desc
            app_desc = 'null'
            #获取creat_time
            # create_time = app1_detail['last_update'].encode('utf8', 'ignore')
            create_time = '2014-3-14'
            #Mysql数据库
            app_info=[app_version,app_name,app_package,app_icon,app_size,app_type,app_from,app_url,app_desc,platform,create_time]
            
            app_infos.append(app_info)
        flag=False
    return app_infos

def get_app_num():
    app_num=redis_client.get_length('app::data')
    print 'app_num:'+str(app_num)
    return app_num