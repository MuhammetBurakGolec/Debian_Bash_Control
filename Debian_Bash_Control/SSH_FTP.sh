#!/bin/bash

clear
echo Starting "SSH And FTP Control" v1.0 
#All Services Stop
sudo service ssh stop
sudo service vsftpd stop
sudo service tor stop
sudo service cups stop
echo All Ports Closed 
sleep 0.5
#Clear Trash
rm -Rf ~/.Trash/*
echo Trash Cleared
sleep 0.5
#Start Service
sudo service ssh start
sudo service vsftpd start
echo SSH And FTP Services Starting  
#Finished
sleep 0.5
echo Done...
sleep 1
clear
nmap 127.0.0.1 -Pn
sleep 5
clear



