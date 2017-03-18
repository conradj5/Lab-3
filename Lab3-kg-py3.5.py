import win32api
from subprocess import Popen, PIPE
     
# Password 1 #
print(''.join( chr(ord("ABCDEF123456"[i]) + 5) for i in range(0, 12)))

# Password 2 #
print(''.join( chr(ord("ARCHIEMILLER"[i]) - i) for i in range(0, 12)))

# Password 3 #
print(''.join( chr(ord("GO FLYERS!!!"[i]) ^ i) for i in range(0, 12)))

# Password 4 #
print(win32api.GetVolumeInformation("C:\\")[1])

# Passwrod 5 #
print(Popen("Pass5.exe", shell=True, stdout=PIPE).communicate()[0])
