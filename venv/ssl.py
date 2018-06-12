#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
from Tkinter import *
from tkMessageBox import *
from time import sleep
#import logging
import os
import argparse
import signal
import sys
import re


flag = False

def answer():
    #global window
    global flag
    #s.send_header('Location', 'https://www.google.com')
    print "self in answer is:"
    #print s.path
    flag = False
    #window.quit()

#window = Tk()



def callback():
    time_to_sleep = 1
    flushIPTables()
    sleep(time_to_sleep * 60)
    defineIPTable()
    print "we on the line again!\n"


def signal_handler(signal, frame):
    flushIPTables()
    print('\nYou have been warned!\n')
    sys.exit(0)


def redirect_factory():
    class RedirectServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
            #global window
            global flag

            str1 = str(self.headers)[6:str(self.headers).find('\r\n')]
            print str1
            self.send_response(301)


            if is_ssl_verify('www.' + str1):
                print "first"
                self.send_header('Location', 'https://www.' + str1)
            elif is_ssl_verify(str1):
                print "second"
                self.send_header('Location', 'https://' + str1)
            else:

                #Button(text='PAUSE', command=quit).pack()
                #Button(text='OK', command=answer).pack()
                print "else"
                print self.path
                self.send_header('Location', 'https://www.google.com')
                #mainloop()
                print "end gui"

            self.end_headers()
    return RedirectServer

def defineIPTable():
    os.system('sudo echo 1 > /proc/sys/net/ipv4/ip_forward')
    os.system('sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j DNAT --to-destination 127.0.0.1')

def flushIPTables():
    os.system('sudo iptables -t nat -F')
    os.system('sudo iptables -F')
    os.system('sudo echo 0 > /proc/sys/net/ipv4/ip_forward')

def is_ssl_verify(url):
    os.system('echo QUIT | openssl s_client -connect %s:443 -showcerts > output.txt 2>/dev/null & sleep 2' % url)
    if os.stat("output.txt").st_size == 0:
        return False
    return True

def isNumber(port):
  try:
    int(port)
    return True
  except:
    return False

def main():

    parser = argparse.ArgumentParser(description='HTTP redirect to HTTPS')
    parser.add_argument('--port', '-p', action="store", type=int, default=80, help='port to listen on')
    parser.add_argument('--ip', '-i', action="store", default='', help='host interface to listen on')

    myargs = parser.parse_args()
    port = myargs.port
    host = myargs.ip

    if not isNumber(port):
        print "invalid port"
        sys.exit(0)

    is_valid_ip = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", host)
    if not is_valid_ip and host != '':
        print "invalid ip"
        sys.exit(0)


    #ip_format = re.compile(host)
    #if ip_format.match('xx:xx:xx:xx')

    defineIPTable()

    redirectServer = redirect_factory()
    handler = SocketServer.TCPServer((host, port), redirectServer)
    print("serving at port %s" % port)

    handler.serve_forever()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
    #signal.pause()