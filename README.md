# sslUnStrip
-- SSL Strip Defense --

You can visit us in :
https://github.com/nirkai/sslUnStrip

This file is instructions for simple use in the sslUnStrip.py program.

_Goal:_   
Protect the internet surfing from ssl strip attack.

It requires Python 2.7 or newer, not special modules requires.
Currently run only on Linux OS.

_Installing:_  
	Not require.

_Running:_  
	sslUnStrip is a python script.
	To use it, just download it and type in terminal (in the file's directory):

	chmod +x ssl.py
	./ssl.py

_parser flags:_


	usage: ssl.py [-h] [--port PORT] [--ip IP] [--search SEARCH]
	
	HTTP redirect to HTTPS
	optional arguments:
	  -h, --help            show this help message and exit
	  --port PORT, -p PORT  port to listen on
	  --ip IP, -i IP        host interface to listen on
	  --search SEARCH, -s SEARCH
				search the word in openssl answer

_Exit:_  
	To end the program just press on `ctl+c` in terminal, as keyboard-interupt.

_Notice !_  
	-	The sslUnStrip program add an iptables rule to OUTPUT chain in nat table.  
	-	It also allow redirect packets.  
	-	If there is a long stay because of the lan OR the web we search for don't secure, we will return to safety site.  
	-	At the end of the program, by pressing `ctl+c`, it flush all the new rules from the iptables, and not allow redirect packets.  
	-	The parser is preparation of infrastructure for future implementation, so don't use the `-p` and `-i` flags right now.  
	-	The search flag is for high security level (experience users only). For example, if you will enter `./ssl.py -s "class 3"` it will let you to surf only to websites with class 3 level security.  
