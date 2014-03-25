#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
reload(sys)
c_path = os.getcwd()
base_path=c_path[:c_path.rfind("RedistoMySQL")]
sys.path.append(base_path)
from RedistoMySQL.src.util import RedisUtil
from RedistoMySQL.src.util import CommonUtil

redis_client = RedisUtil.RedisClient()

#通过download_time获取app信息，传入起始和终止数，返回一个list
def get_app_info_bydownload(startnums,endnums,app_total):
    
    app_lists = redis_client.get_items('app::data',startnums,endnums)
    app_infos=[]
    for app in app_lists:
        app = eval(app)
        flag=False
        #获取app详细信息type=list
        app_details = app['app_detail']
        for app_detail in app_details:
            #获取download_times
            app_download_times=app_detail['download_times'].encode('utf8', 'ignore')
                
            app_download_times=CommonUtil.download_time_normalize(app_download_times)
            print app_download_times
            if int(app_download_times)>=10000000:
                flag=True
            
        if flag==True:
        

            #app名称
            app_name = app['app_name'].encode('utf8', 'ignore')
            #app类型3200:9999,1100:1
            app_type = app['category'].encode('utf8', 'ignore')
            #获取app的package_name
            app_package = app['package_name'].encode('utf8', 'ignore')
            
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
            
            app_download_times=CommonUtil.download_time_normalize(app_download_times)
            print app_download_times
            #获取cover
            cover=app_detail['cover'].encode('utf8', 'ignore')
            #获取creat_time
            # create_time = app1_detail['last_update'].encode('utf8', 'ignore')
            create_time = '2014-3-14'
            #Mysql数据库
            app_info=[app_version,app_name,app_package,app_icon,app_size,app_type,app_from,app_url,app_desc,platform,create_time]
            
            app_infos.append(app_info)

            #下载app_icon_file
            #CommonUtil.download_icon(cover,app_name)
        flag=False
    
    return app_infos


#通过category获取app信息，传入起始和终止数，返回一个list
def get_app_info_bycategory(startnums,endnums,app_total):
    
    app_lists = redis_client.get_items('app::data',startnums,endnums)
    app_infos=[]
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
        if num>=4:
            app_type=app_type[0].split(':')+':'+num
            print app_type
            flag=True
        if flag==True:
        

            #app名称
            app_name = app['app_name'].encode('utf8', 'ignore')
            #app类型3200:9999,1100:1
            app_type = app['category'].encode('utf8', 'ignore')
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
        flag=False
    if len(app_infos)>=app_total:
        #对app_info排序
        app_infos.sort(key=lambda x:int(x.split(':')[1]))
        app_infos=app_infos[:app_total]
    return app_infos

#获取当前app总数
def get_app_num():
    app_num=redis_client.get_length('app::data')
    print 'app_num:'+str(app_num)
    return app_num