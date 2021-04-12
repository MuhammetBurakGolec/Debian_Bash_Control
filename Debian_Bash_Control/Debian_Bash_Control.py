#UTF-8 Charset
#/usr/bin/Python3.9
# Author = Muhammet Burak Golec

try:
    

    import time
    import os
    from colorama import  Fore, Back, Style

except ImportError as error:
    
    print("Import Error..")
    time.sleep(5)
    exit



os.system("clear")
print(Fore.RED +"Yapılacak İşlemi Seçiniz")
print("")
print(Fore.GREEN +"1 - UPDATE")
print("")
print(Fore.GREEN +"2 - SSH_FTP")
print("")
print(Fore.GREEN +"3 - UPDATE & SSH_FTP")
print("")
print(Fore.GREEN +"4 - PROGRAMS")
print("")
print(Fore.GREEN +"5 - BOOTNET")
print("")
print(Fore.GREEN +"6 - CLOSE BOOTNET")
print("")
print(Fore.GREEN +"7 - ALL PORT CLOSED")
print("")
bash = input(Fore.BLACK + Back.WHITE + "cmd$ >" + Style.RESET_ALL + Fore.BLUE)
eval(bash)
bash = int(bash)

print(Style.RESET_ALL + "")

    
if bash == 1 :
    os.system("bash /usr/local/sbin/UPDATE.sh")
    
elif bash == 2 :
    os.system("bash /usr/local/sbin/SSH_FTP.sh")

elif bash == 3 :
    os.system("bash /usr/local/sbin/UPDATE.sh")
    os.system("bash /usr/local/sbin/SSH_FTP.sh")

elif bash == 4 :
    os.system("bash /usr/local/sbin/PROGRAMS.sh")

elif bash == 5 :
    os.system("bash /usr/local/sbin/BOOTNET.sh")

elif bash == 6 :
    os.system("clear")
    os.system("sudo anonsurf stop")
    os.system("clear")
    os.system("neofetch")

elif bash == 7 :



    os.system("bash /usr/local/sbin/ALL_CLOSED.sh")
