#!/usr/bin/env python

import os
import struct
    
if os.getuid() != 0:
    print "Sorry, root permission required."
    exit(1)

try:
    import psutil
except:
    print "You need to have sysutils/py-psutil installed."
    exit (2)

def parseram(val):
    if val > 1073741824:
        return str(val/1073741824)+" GiB"
    if val > 1048576:
        return str(val/1048576)+" MiB"
        
    if val > 1024:
        return str(val/1024)+" KiB"
        
    return str(val)+" B"
    
processes = psutil.get_process_list()

print "Memory       %Usage        PID     Name"
for p in processes:
    p = psutil.Process(p.pid)
    line = ""
    line += parseram(p.get_memory_info().rss)
    while len(line) < 13:
        line += " "
        
    line += str(p.get_memory_percent())[:10]
    while len(line) < 27:
        line += " "
    line += str(p.pid)
    while len(line) < 35:
        line += " "
            
    line += p.name
    try:
        print line
    except:
        pass

