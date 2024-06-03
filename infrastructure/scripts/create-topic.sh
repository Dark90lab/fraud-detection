#!/usr/bin/env bash
source .env

# if [ "$#" -ne 1 ]; then
#     echo "Error: Expected exactly 2 arguments."
#     exit 1 # Exit with a non-zero status to indicate an error
# fi

echo Creating kafka topic Transactions and Frauds

PORT=9092

check_port() {
    nc -z localhost $PORT
    return $?
}
while ! check_port; do
    echo "[CREATE_TOPIC]Port $PORT is not yet occupied, waiting..."
    sleep 1
done

$KAFKA_DIR/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Transactions
$KAFKA_DIR/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Frauds
