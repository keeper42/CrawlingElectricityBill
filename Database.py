# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/04/30
# This function is the definition of the database

import pymysql

# Set the information of database
connect = pymysql.connect(
	host = '127.0.0.1',
	user = 'username',
	passwd = 'password',
	db = 'electricity_bill',
	charset = 'utf8'
)