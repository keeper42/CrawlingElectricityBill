# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/04/29
# The first time to modify: 2017/05/01
# This is the main function file

import time
import datetime
import threading
import pymysql
import Database
import CrawlingFunction

#
#
# Main part
#
#
# Connect to the database
connect = Database.connect

# Set the cursor
cursor = connect.cursor()

# Set headers 
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# Set url
baseUrl = "http://192.168.84.3:9090/cgcSims/login.do?task=station&client="
northCampusUrl = baseUrl + "192.168.84.1"
southCampusUrl = baseUrl + "192.168.84.110"
xiliCampusUrl = baseUrl + "172.21.101.11"

# Start the timer
start = datetime.datetime.now()

# Crawl and store electricity bill information of all campuses, what's more, calculate the time required to execute the function
# Crawl the xili campus' electricity bill information and calculate the time required to execute the function
CrawlingFunction.CrawlElectricityInfoOfXiliCampus(xiliCampusUrl, headers, cursor, connect)

# Crawl the south campus' electricity bill information and calculate the time required to execute the function
CrawlingFunction.CrawlElectricityInfoOfSouthCampus(southCampusUrl, headers, cursor, connect)

# Crawl the north campus' electricity bill information and calculate the time required to execute the function
for area in range(3):
	CrawlingFunction.CrawlElectricityInfoOfNorthCampus(northCampusUrl, headers, cursor, connect, area)

# time.sleep(3)
#
#
# Here has not achieved multi-threaded crawling function yet.
#
#
# End the timer
end = datetime.datetime.now()

print("The program is time consuming: " + str(end - start))

# Close cursor and connect
cursor.close()
connect.close()

#
#
# End Main part
#
#