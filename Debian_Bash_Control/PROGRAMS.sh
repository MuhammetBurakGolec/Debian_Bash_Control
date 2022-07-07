clear
sudo apt-get install vlc
sudo apt-get install mousepad
sudo apt-get install net-tools
sudo apt-get install snap
sudo apt-get install curl
sudo apt-get install nmap
sudo apt-get install wireshark
sudo apt-get install netcat
sudo apt-get install qbittorrent
sudo apt-get install unzip
sudo apt-get install tar
sudo apt-get install filezilla
sudo apt-get install vsftpd
sudo apt-get install ssh
sudo apt-get install python3
sudo apt-get install pip3
sudo apt-get install tmux
sudo apt-get install python
sudo snap install --classic sublime-text
sudo snap install --classic code
sudo snap install spotify

read -p "Do You Want to Install Libre Office ? [ Y / N ]" question
question = ${questio^^}
if (($question == 'Y' )) || (( ${question^^} =='YES')) 
    then sudo snap install libreoffice
fi
clear








