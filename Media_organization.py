import os
import sys

imgTypes = ['.jpg', 'jpeg', '.png']
vdoTypes = ['.mp4', '.avi', '.3gp', '.mpeg', '.mkv', '.wmv', '.mov']

def type_check(file):
    for t in imgTypes:
        if file.endswith(t):
            return 'photo'
    for v in vdoTypes:
        if file.endswith(v):
            return 'video'
    os.remove(adrs)

from datetime import datetime
def date(path):
    time = os.path.getmtime(path)
    return datetime.fromtimestamp(time).year
        
path = 'E:\\Offices\\Pourshafiei'
src = 'E:\\Offices\\Pourshafiei'
dst ='E:\\Offices\\purTest'
#print(type_check(path.split('\\')[-1],path))
#print(date(path))
os.chdir(path)
rmv_list = []
for obj in os.walk(path):
    for file in obj[2]:
        date = date(file)
        if not os.path.exists(str(date)):
            os.mkdir(str(date))
        addrs = os.path.join(obj[0],str(date))
        type_file = type_check(file)
        #if not os.path.isdir(os.path.join(obj[0],type_file)):
        if not type_file:
            continue
        if not os.path.exists(os.path.join(str(date),type_file)):
            os.mkdir(os.path.join(str(date),type_file))
        file.close()
        os.rename(path,dst)
        
        
