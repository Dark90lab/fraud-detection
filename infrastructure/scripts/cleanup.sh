#!/usr/bin/env bash
source .env

echo Kafka dir: $KAFKA_DIR

exit_code=$?
kafka_command=$KAFKA_DIR/bin/kafka-server-stop.sh
zookeeper_command=$KAFKA_DIR/bin/zookeeper-server-stop.sh
flink_command=$FLINK_DIR/libexec/bin/stop-cluster.sh
PID=$(lsof -t -i:9000)

directory_to_remove=./~

# Check if the directory exists
if [ -d "$directory_to_remove" ]; then
    echo Log directory exists. Removing...
    # Remove the directory
    rm -rf $directory_to_remove
    echo Directory removed successfully.
else
    echo $directory_to_remove: Directory does not exist.
fi

echo Stopping kafka...
$kafka_command

echo Stopping zookeeper...
$zookeeper_command

echo Stopping flink...
$flink_command

echo Stopping kafdrop...
if [ -n "$PID" ]; then
    echo "Killing process $PID"
    kill $PID
else
    echo "No process found"
fi

echo Cleanup Sucessfully...
