#!/bin/bash
#Author : Muhammet Burak Golec


Debian ="sudo apt-get update &&  sudo apt-get upgrade -y && sudo apt-get autoremove -y "
Op_Sys="`uname`"

case $Op_Sys in 
'Linux') OS='Linux' shopt -s nocasematch;

        if [[ $os =~ "debian" ]]; then
            echo "Debian"
        elif [[ "$os" =~ "ubuntu" ]]; then
            echo "Ubuntu"
        elif [[ "$os" =~ "centos" ]]; then
            echo "Centos"
        else
        echo "unknown os: $os"
        exit 1
        fi 

        if [[ ! -z $YUM_CMD ]]; then
            sudo yum update && sudo yum upgrade
        elif [[ ! -z $APT_GET_CMD ]]; then
            apt-get $DEB_PACKAGE_NAME
        elif [[ ! -z $OTHER_CMD ]]; then
            $OTHER_CMD continue
        else
            echo "error can't install package $PACKAGE"
            exit 1;
        fi
    ;;
  'FreeBSD') OS='FreeBSD' echo "FreeBSD"
    ;;
  'WindowsNT') OS='Windows' echo "Does not work in Windows"
    ;;
  'Darwin') OS='Mac' echo "Darwin needed brew" # Will be soon
    ;;
  'SunOS') OS='Solaris' echo "Solaris"
    ;;
  *) ;;
esac


