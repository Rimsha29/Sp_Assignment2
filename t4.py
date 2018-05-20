import psutil 
import time
import sys
import os

try :
	p = psutil.Process(int(sys.argv[1]))
	
except:
	print "not right arguments"
else:
	print "process ID: ", p.pid
	print "process Name: ", p.name()
	print "process Status: ", p.status()
	print "process Parent ID: ", p.ppid()
	pname=psutil.Process(p.ppid())
	proname=str(pname.name())
	print ("process Parent Name: " +proname)
	print "Process Creation Time:", time.ctime(p.create_time())
	#print "Files opened by the process info:", p.get_open_files()
	mem=str(p.memory_info())
	pm=mem[9:(len(mem)-1)]
	prom=pm.split(",")
	print ("Memory Info (In Bytes):")
	print(" ".join(prom))



