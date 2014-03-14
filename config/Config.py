#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


MySQL={
	'host':'localhost',
	'password':'123456',
	'user':'root',
	'db':'test',
	'charset':'utf8',
	'port':3306
}