#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
reload(sys)
c_path = os.getcwd()
base_path=c_path[:c_path.rfind("RedistoMySQL")]
sys.path.append(base_path)
import urllib
from RedistoMySQL.src.util import RedisUtil
redis_client = RedisUtil.RedisClient()
#下载app_icon文件 用appid作为文件名
def download_icon(url,appname):
	icon_id=redis_client.hget('app::index', appname)
	if not os.path.exists('icon/'): os.makedirs('icon/')
	urllib.urlretrieve(url,'icon/'+icon_id+'.jpg')
	print appname+'的icon下载完成'

# url='http://file.market.xiaomi.com/thumbnail/PNG/l80/AppStore/e134c6cd-1059-4018-a8b1-efd831e8e25d'
# download_icon(url,'随手优惠(淘宝省钱)')


'''
	对download_time进行格式化
'''
def download_time_normalize(download_time):
    '''
    有些网站中的下载次数不是纯数字，所以要对其中的字符串进行替换操作，从而可以统一格式
    '''
    
    download_time=download_time.replace('+','')
    download_time=download_time.replace('小于','')
    download_time=download_time.replace('-','')
    download_time=download_time.replace(' ','')
    if download_time.find('.')<0:
        download_time=download_time.replace('万','0000')
        download_time=download_time.replace('千','000')
        download_time=download_time.replace('千万','00000000')
        download_time=download_time.replace('亿','000000000')
    if download_time.find('千万')>0:
        download_time=str(int(float(download_time[0:download_time.find('千')])*10000000))
    if download_time.find('千')>0:
        download_time=str(int(float(download_time[0:download_time.find('千')])*1000))
    if download_time.find('万')>0:
        download_time=str(int(float(download_time[0:download_time.find('万')])*10000))
    if download_time.find('亿')>0:
        download_time=str(int(float(download_time[0:download_time.find('亿')])*100000000))
    if download_time=='':
    	download_time=0
    return download_time

