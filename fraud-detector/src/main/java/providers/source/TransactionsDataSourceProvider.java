package providers.source;

import mappers.TransactionDeserializationSchema;
import models.Transaction;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import providers.config.ConfigProvider;

import java.util.Properties;

public class TransactionsDataSourceProvider implements  IDataSourceProvider<Transaction>{
    @Override
    public DataStream<Transaction> getSourceStream(StreamExecutionEnvironment env) {
        return env.addSource((new FlinkKafkaConsumer<>(ConfigProvider.getInstance().kafkaConfig.SourceTopic, new TransactionDeserializationSchema(), KafkaProperties.getProperties())).setStartFromEarliest());
    }
}
