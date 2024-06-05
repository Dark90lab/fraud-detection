#!/usr/bin/env bash
source .env

flink_command=$FLINK_DIR/libexec/bin/stop-cluster.sh

echo Stopping flink...
$flink_command
