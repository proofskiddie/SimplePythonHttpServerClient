import socket
from sys import *
from os.path import dirname, realpath, join, exists
from os import makedirs

nargs = len(argv)
if nargs not in [3,4]: 
	print "Usage: client.py [server_host][server_port][filename = \"/\"]"
	exit(0)

HOST     = argv[1]   
PORT     = int(argv[2])
if nargs == 3: FILENAME = "/"
else         : FILENAME = argv[3]
request = "GET " + FILENAME + " HTTP/1.1\r\n"

if FILENAME == "/": newfile = 'index.html'
else: 		    newfile = FILENAME

tpath = join(realpath('.'), 'Downloads')
if not exists(tpath): makedirs(tpath)

tpath = join(tpath,newfile)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendto(request.encode(), (HOST, PORT))
data = s.recv(1024)

fp = open(tpath, 'w+')
fp.write(data.decode())
fp.close()
s.close()

