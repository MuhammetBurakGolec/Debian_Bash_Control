clear
echo Starting "SSH And FTP Control" v1.0 
echo Coding By MOZARTBURAK
#All Services Stop
sudo service ssh stop
sudo service vsftpd stop
sudo service tor stop
sudo service cups stop
echo
echo All  Ports Closed 
sleep 1
#Clear Trash
rm -Rf ~/.Trash/*
echo
echo Trash Cleared
sleep 1
#Start Service
sudo service ssh start
sudo service vsftpd start
echo 
echo SSH And FTP Services Starting  
#Finished
sleep 1 
echo
echo Done...
sleep 1
clear
nmap 127.0.0.1 -Pn
sleep 5
clear



