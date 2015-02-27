#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sqlite3 as mydb

""" Log Current Time, Temperature in Celsius and Fahrenheit
 Returns a list [time, tempC, tempF] """
 
con = None
 
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006973ecf/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	try:
		con = mydb.connect('/home/pi/temperature.db')
		cur = con.cursor()    
		cur.execute("INSERT INTO tempData VALUES(?,?,?);",(currentTime,tempC,tempF))
		con.commit();
		con.close();
    	except mydb.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
    
	finally:
		if con:
			con.close()
		return ("Current temperature is: "+str(tempF)+" F");
print readTemp() 
print ("Temperature logged")