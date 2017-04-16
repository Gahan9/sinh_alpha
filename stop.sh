#!/usr/bin/env bash

PIDFILE=SINH.pid

cd $(dirname $0)

PID=$(cat $PIDFILE 2>/dev/null)

if [ -n "$PID" ]; then
  echo "Stopping SINH...\n"
  kill -TERM $PID
fi
