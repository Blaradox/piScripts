#! /bin/sh

cd /home/pi/Scripts
File=services.txt
if grep -q "VNC: enabled" "$File"; then
	su - pi -c "/usr/bin/vncserver"
	echo VNC server started
fi 
if grep -q "button: enabled" "$File"; then
	python3 /home/pi/Scripts/shutdown_pi.py &
	echo Shutdown button enabled
fi
if grep -q  "lan: enabled" "$File"; then
	python3 /home/pi/Scripts/wakeonlan.py &
	echo Wake On Lan enabled
fi


