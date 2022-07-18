#!/bin/bash
nohup awk 'BEGIN { while (c++<50) print "y" }' >myscript.log 2>&1 &
nohup ./tmp/scripts/init-db.sh >/tmp/scripts/log 2>&1 &
exec docker-entrypoint.sh "$@"
