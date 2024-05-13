#!/usr/bin/env bash
source .env

output_dir=$FLINK_DIR/libexec/lib

declare -A jar_links=(
    ["kafka-clients-3.4.0.jar"]=https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.0/kafka-clients-3.4.0.jar
    ["flink-connector-kafka-3.1.0-1.18.jar"]=https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka/3.1.0-1.18/flink-connector-kafka-3.1.0-1.18.jar
)

if [! -d $output_dir]; then
    echo Flink lib directory does not exist!
    exit
fi

for jar_file in "${!jar_links[@]}"; do
    download_link="${jar_links[$jar_file]}"
    jar_path=$output_dir/$jar_file

    if [ -f "$jar_path" ]; then
        echo "Skipping download. $jar_file already exists in output dir."
    else
        echo "Downloading $jar_file from $download_link..."

        curl -o "$output_dir/$jar_file" "$download_link"
        echo "Downloaded $jar_file"
    fi
done

echo "Download complete."
