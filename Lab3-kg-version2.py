import win32api
from subprocess import Popen, PIPE
     
# Password 1
psw = "ABCDEF123456"
result = ""
for i in range(0, len(psw)):
    result += chr(ord(psw[i])+5)
print result

# Password 2
psw = "ARCHIEMILLER"
result = ""
for i in range(0, len(psw)):
    result += chr(ord(psw[i]) - i)
print result

# Password 3
psw = "GO FLYERS!!!"
result = ""
for i in range(0, len(psw)):
    result += chr(ord(psw[i]) ^ i)
print result

# Password 4
print win32api.GetVolumeInformation("C:\\")[1]

# Password 5
print Popen("Pass5.exe", stdout=PIPE).communicate()[0].strip()
