#!/bin/bash
echo "initializing db..."
sleep 40

cqlsh -u 'cassandra' -p 'cassandra' -f /tmp/scripts/create-admin-user.sql
cqlsh -u 'matt' -p '1234' -f /tmp/scripts/default.sql
echo "done"
