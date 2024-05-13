#!/usr/bin/env bash
source .env

./kafka-run.sh
sleep 5
./kafdrop-run.sh
