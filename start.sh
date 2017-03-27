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

echo "--------------- S.I.N.H v0.1---------------"
echo "Initializing SINH............"

echo "Forwarding port...."
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
twistd -y sinh.tac -l log/sinh.log --pidfile SINH.pid
echo "Honeypot Started Monitoring your device"

echo "Starting Django Service"
python3 ./honeyweb/manage.py runserver 0.0.0.0:8888
