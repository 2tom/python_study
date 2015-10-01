#!/bin/sh

/opt/kibana/bin/kibana -e http://$ELASTIC_PORT_9200_TCP_ADDR:$ELASTIC_PORT_9200_TCP_PORT
while true
do
	sleep 10
done
