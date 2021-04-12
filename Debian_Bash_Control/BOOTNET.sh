while true; do
	
	clear
	echo "Anonsurf Starting"
	sleep 5
	
	clear
	anonsurf start 
	anonsurf restart
	
	clear
	echo "Bootnet Start"
	echo ""
	echo "Ip Adress: " && curl icanhazip.com 
	echo "Revers Dns Record:" && curl icanhazptr.com 
	echo "Traceroute:" && curl icanhaztrace.com
	echo "Wait 30 Seconds"
	
	sleep 30 
done

