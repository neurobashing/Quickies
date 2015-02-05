#!/usr/bin/env python

import os
# We want to scan for 2 types of log entries:
# Dec 16 09:20:25 pop vpopmail[8164]: vchkpw-smtp: password fail (pass: 'jim.norton') jim.norton@asti-usa.com:37.235.209.102
# Dec 16 09:20:19 pop vpopmail[8162]: vchkpw-smtp: vpopmail user not found jim.norton@:37.235.209.102

safelist = ['173.73.3.108']


def chopline(linestring):
    badpart = linestring.split()[-1]
    ipaddr = badpart.split(':')[-1]
    return ipaddr

# maintain a list of already blocked IPs
blockfile = open('blocked_list', 'a+')
iplist = blockfile.readlines()
blocked_ips = []
for item in iplist:
    blocked_ips.append(item.strip())
# read the logfile into lines
logfile = open('/var/log/maillog', 'r').readlines()

for line in logfile:
    if 'password fail' in line:
        block_ip = chopline(line)
    elif 'user not found' in line:
        block_ip = chopline(line)
    else:
        block_ip = False
    if block_ip:
        if block_ip in safelist:
            print "not going to block ASTi"
            pass
        else:
            if block_ip not in blocked_ips:
                os.system('/sbin/iptables -I INPUT 1 -s ' + block_ip + ' -j DROP')
                blockfile.write(block_ip + "\n")
                blocked_ips.append(block_ip)
            else:
                pass
blockfile.close()
