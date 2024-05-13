#!/usr/bin/env bash
source .env

./flink-get-dependecies.sh

$FLINK_DIR/libexec/bin/stop-cluster.sh

$FLINK_DIR/libexec/bin/start-cluster.sh
