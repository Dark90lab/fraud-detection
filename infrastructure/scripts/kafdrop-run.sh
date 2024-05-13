#!/usr/bin/env bash
source .env

PORT=9092

echo Runing Kafdrop...

PORT=9092

check_port() {
    nc -z localhost $PORT
    return $?
}

while ! check_port; do
    echo "[KAFDROP]Port $PORT is not yet occupied, waiting..."
    sleep 1
done

sleep 3

# JAVA=/Library/Java/JavaVirtualMachines/jdk-11.jdk/Contents/Home/bin/java

$JAVA_11_BIN_PATH --add-opens=java.base/sun.nio.ch=ALL-UNNAMED \
    -jar /Users/grzelakm/kafdrop-3.29.0.jar \
    --kafka.brokerConnect=localhost:$PORT
