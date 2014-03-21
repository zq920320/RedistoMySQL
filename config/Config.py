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