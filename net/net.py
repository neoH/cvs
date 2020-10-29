#! /usr/bin/env python3

import psutil;
import netifaces;

import sys;

##info = psutil.net_io_counters();
##
##
##print ("type(info)=",type(info));
##print ("bytes sent=",info.bytes_sent);
##print ("bytes recv=",info.bytes_recv);
##
##
##import urllib;


print (netifaces.interfaces());

gwi = netifaces.gateways();
print (gwi);


import socket;

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

saddr = '192.168.50.11';
print ("connecting to ",saddr);
s.connect((saddr,8088));

print ("s=",s);

rcv = 'hello from client';

s.send(rcv.encode('utf-8'));





print ("exit 0");
sys.exit(0);
