package org.example;
import detectors.ValueTresholdFraudDetector;
import models.Transaction;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import providers.source.FraudsSinkProvider;
import providers.source.IDataSourceProvider;
import providers.source.ISinkProvider;
import providers.source.TransactionsDataSourceProvider;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class FraudsDetector {
    private static final Logger LOG = LoggerFactory.getLogger(FraudsDetector.class);

    public static void main(String[] args) throws Exception {

        LOG.info("Starting Frauds Detector");

        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        IDataSourceProvider<Transaction> transactionsSourceProvider = new TransactionsDataSourceProvider();
        ISinkProvider<Transaction> sinkProvider = new FraudsSinkProvider();

        DataStream<Transaction> sourceStream = transactionsSourceProvider.getSourceStream(env)
                .keyBy(Transaction::getUserid)
                .process(new ValueTresholdFraudDetector());

//        sourceStream.map(value -> {
//            LOG.info("Processing value: {}", value.id);
//            return  value;
//        });

        sinkProvider.sink(sourceStream);

//        FlinkKafkaConsumer<TemperatureReading> temperatureConsumer = new FlinkKafkaConsumer<>(ReadTopic, new TemperatureDeserializationSchema(), GetKafkaProperties());
//
//        FlinkKafkaProducer<String> alarmProducer = new FlinkKafkaProducer<>(WriteTopic, new SimpleStringSchema(),GetKafkaProperties());
//
//        DataStream<TemperatureReading> temperatureStream = env.addSource(temperatureConsumer.setStartFromEarliest());
//
//        DataStream<String> alarmStream = temperatureStream.filter(new FilterFunction<TemperatureReading>() {
//            @Override
//            public boolean filter(TemperatureReading reading) throws Exception {
//                return reading.temperature < 0;
//            }
//        }).map(reading -> "Alarm " + reading.id + " " + reading.timestamp + " " + reading.temperature);
//
//
//        alarmStream.addSink(alarmProducer);
//
        env.execute("Frauds Detector");
    }

//    public static class TemperatureReading {
//        public int id;
//        public String timestamp;
//        public int temperature;
//    }

//    public static class TemperatureDeserializationSchema implements DeserializationSchema<TemperatureReading> {
//
//        @Override
//        public TemperatureReading deserialize(byte[] message) throws IOException {
//            String jsonString = new String(message, StandardCharsets.UTF_8);
//
//            ObjectMapper mapper = new ObjectMapper();
//            return mapper.readValue(jsonString, TemperatureReading.class);
//        }
//
//        @Override
//        public boolean isEndOfStream(TemperatureReading nextElement) {
//            return false;
//        }
//
//        @Override
//        public TypeInformation<TemperatureReading> getProducedType() {
//            return TypeInformation.of(TemperatureReading.class);
//        }
//    }

}