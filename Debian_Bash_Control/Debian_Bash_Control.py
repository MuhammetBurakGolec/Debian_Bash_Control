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

bool = True
while bool == True :

    os.system("clear")
    print(Fore.RED +"Yapılacak İşlemi Seçiniz")
    print("")
    print(Fore.GREEN +"1 - UPDATE")
    print("")
    print(Fore.GREEN +"2 - SSH_FTP")
    print("")
    print(Fore.GREEN +"3 - UPDATE & SSH_FTP")
    print("")
    print(Fore.MAGENTA +"4 - PROGRAMS")
    print("")
    print(Fore.LIGHTCYAN_EX +"5 - BOOTNET")
    print("")
    print(Fore.LIGHTCYAN_EX +"6 - CLOSE BOOTNET")
    print("")
    print(Fore.BLUE +"7 - ALL PORT CLOSED")
    print("")
    print(Fore.LIGHTYELLOW_EX +"8 - QUIT PROGRAM")
    print("")
    bash = input(Fore.LIGHTRED_EX + Back.WHITE + "cmd$ >" + Style.RESET_ALL + Fore.BLUE)
    eval(bash)
    bash = int(bash)

    print(Style.RESET_ALL + "")

    
    if bash == 1 :
        os.system("bash /$HOME/Debian_Bash_Control/UPDATE.sh")
    
    elif bash == 2 :
        os.system("bash /$HOME/Debian_Bash_Control/SSH_FTP.sh")

    elif bash == 3 :
        os.system("bash /$HOME/Debian_Bash_Control/UPDATE.sh")
        os.system("bash /$HOME/Debian_Bash_Control/SSH_FTP.sh")

    elif bash == 4 :
        os.system("bash /$HOME/Debian_Bash_Control/PROGRAMS.sh")

    elif bash == 5 :
        os.system("bash /$HOME/Debian_Bash_Control/BOOTNET.sh")

    elif bash == 6 :
        os.system("clear")
        os.system("sudo anonsurf stop")
        os.system("clear")
        os.system("neofetch")

    elif bash == 7 :
        os.system("bash /$HOME/Debian_Bash_Control/ALL_CLOSED.sh")
    elif bash == 8 :
        bool = False
os.system("clear")
