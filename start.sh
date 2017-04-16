#!/usr/bin/env bash

sudo ./stop.sh

#Ensure Pythonpath is set
export PYTHONPATH=$PYTHONPATH:./sinh:./sinh/core

#Ensure UNIX Shell command path
export PATH=$PATH:/sbin:/bin:/usr/sbin:/usr/bin

#PROCEDURE to activate fake environment
set -e

cd $(dirname $0)

if [ "$1" != "" ]
then
    VENV="$1"

    if [ ! -d "$VENV" ]
    then
        echo "The specified virtualenv \"$VENV\" was not found!"
        exit 1
    fi

    if [ ! -f "$VENV/bin/activate" ]
    then
        echo "The specified virtualenv \"$VENV\" was not found!"
        exit 2
    fi

    echo "Activating virtualenv \"$VENV\""
    . $VENV/bin/activate
fi


toilet -f bigmono9 -F gay -F border:gay S.I.N.H.
#echo "--------------- S.I.N.H v0.1---------------"
toilet -f slant "S.I.N.H v0.1" | boxes -d whirly | lolcat
#echo "Initializing ...." | cowsay -f tux | lolcat
echo "Initializing ...."

echo "Forwarding port...."
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
twistd -y sinh.tac -l log/sinh.log --pidfile SINH.pid
echo "Started Monitoring Service" | cowsay -f tux | lolcat

#toilet -f bigmono9 -F metal S.I.N.H. UI
toilet -f slant "S.I.N.H UI" | boxes -d columns | lolcat
echo "Enabling Web Framework to view log" | boxes -d columns | lolcat
python3 ./honeyweb/manage.py runserver 0.0.0.0:8888
