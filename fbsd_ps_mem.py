#!/usr/bin/env python

#  Copyright (c) 2011 Jakub Szafrański <samu@pirc.pl>
#
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
#  OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
#  OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
#  SUCH DAMAGE.
 
#  fbsd_ps_mem.py
#  FreeBSD process memory usage monitoring tool.

import os
    
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

