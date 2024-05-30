package providers.source;

import mappers.TransactionSerializationSchema;
import models.Transaction;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSink;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;
import providers.config.ConfigProvider;

public class FraudsSinkProvider implements ISinkProvider<Transaction>{
    @Override
    public DataStreamSink<Transaction> sink(DataStream<Transaction> stream)
    {
       return stream.addSink(new FlinkKafkaProducer<>(ConfigProvider.getInstance().kafkaConfig.SinkTopic, new TransactionSerializationSchema(),KafkaProperties.getProperties())).name("Frauds Kafka Sink");
    }
}
