from datetime import datetime as dt
from datetime import timezone
utc_dt=dt.now(timezone.utc)
l_dt=utc_dt.astimezone()
try:
    openlog=open("log.txt","x")
    openlog.close()
    #openlog = open("log.txt","a+")
except:
    openlog=open("log.txt","w")
    openlog.write("")
    openlog.close()
def log_sto(info):
    openlog = open("log.txt","a+")
    openlog.write(info+"["+l_dt.now().strftime("%H:%M:%S")+"]"+"<br>")
    openlog.seek(0)
    return openlog.read()
