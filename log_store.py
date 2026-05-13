'''
<<<<<<< HEAD

=======
>>>>>>> 20de0da523b94548546924a1263782882528cd55
'''
from datetime import datetime as dt
from datetime import timezone
utc_dt=dt.now(timezone.utc)
l_dt=utc_dt.astimezone()

partial_l=""

try:
    openlog=open("log.txt","x")
    openlog.close()
    #openlog = open("log.txt","a+")
except:
    openlog=open("log.txt","w")
    openlog.write("")
    openlog.close()
def log_sto(info):
    partial_log=""
    openlog = open("log.txt","a+")
    openlog.write(info+"["+l_dt.now().strftime("%H:%M:%S")+"]"+"<br>\n")
    openlog.seek(0)
    for i in openlog.readlines()[-32:]:
        partial_log+=i.replace("\n","")
    return partial_log
def gimmefull():
    read=open("log.txt","r")
    return read.read()
    openlog = open("log.txt","a+")
    openlog.write(info+"["+l_dt.now().strftime("%H:%M:%S")+"]"+"<br>")
    openlog.seek(0)
    return openlog.read()

