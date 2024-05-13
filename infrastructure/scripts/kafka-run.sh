#!/usr/bin/env bash

source .env

echo Cleanup..

./cleanup.sh

PORT=2181

check_port() {
    nc -z localhost $PORT
    return $?
}

echo Running Zookeeper...
$KAFKA_DIR/bin/zookeeper-server-start.sh $KAFKA_DIR/config/zookeeper.properties &

while ! check_port; do
    echo "Port $PORT is not yet occupied, waiting..."
    sleep 1
done

sleep 5
echo Running Kafka...
$KAFKA_DIR/bin/kafka-server-start.sh $KAFKA_DIR/config/server.properties &

echo Running Kafdrop...
./kafdrop-run.sh
