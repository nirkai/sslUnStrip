# sslUnStrip
-- SSL Strip Defense --

You can find us also in :
https://github.com/nirkai/sslUnStrip

This file is instructions for simple use in the sslUnStrip.py program.

_Goal:_ Protect the ןnternet surfing from ssl strip attack.

It requires Python 2.7 or newer, not special modules requires.
Currently run only on Linux OS.

_Installing:_
	Not require.

_Running:_
	sslUnStrip is a python script.
	To use our it just download it, and type in terminal (in the directory's file):

	chmod +x ssl.py
	./ssl.py

_Exit:_
	To end the program just press on `ctl+c`, as keyboard-interupt.

_Attention !_
	-	The sslUnStrip program add to iptables rule to OUTPUT chain in nat table.
	-	It also allow redirect packets.
	-	At the end of the program, by pressing `ctl+c`, it flush all the new rules from the iptables, and not allow redirect packets.
