package org.example;
import org.apache.flink.api.common.functions.FilterFunction;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Properties;

public class KafkaConsumer {
   private static final String ReadTopic = "Temperatura";
   private static final String WriteTopic = "Alarm";

   public static void main(String[] args) throws Exception {
       final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

       FlinkKafkaConsumer<TemperatureReading> temperatureConsumer = new FlinkKafkaConsumer<>(ReadTopic, new TemperatureDeserializationSchema(), GetKafkaProperties());

       FlinkKafkaProducer<String> alarmProducer = new FlinkKafkaProducer<>(WriteTopic, new SimpleStringSchema(),GetKafkaProperties());

       DataStream<TemperatureReading> temperatureStream = env.addSource(temperatureConsumer.setStartFromEarliest());

       DataStream<String> alarmStream = temperatureStream.filter(new FilterFunction<TemperatureReading>() {
           @Override
           public boolean filter(TemperatureReading reading) throws Exception {
               return reading.temperature < 0;
           }
       }).map(reading -> "Alarm " + reading.id + " " + reading.timestamp + " " + reading.temperature);

       alarmStream.print();
       alarmStream.addSink(alarmProducer);
       alarmStream.print();

       env.execute("Temperature Alarm Processor");
   }

   private static Properties GetKafkaProperties()
   {
       Properties properties = new Properties();
       properties.setProperty("bootstrap.servers", "localhost:9092");

       return properties;
   }

   public static class TemperatureReading {
       public int id;
       public String timestamp;
       public int temperature;
   }

   public static class TemperatureDeserializationSchema implements DeserializationSchema<TemperatureReading> {

       @Override
       public TemperatureReading deserialize(byte[] message) throws IOException {
           String jsonString = new String(message, StandardCharsets.UTF_8);

           ObjectMapper mapper = new ObjectMapper();
           return mapper.readValue(jsonString, TemperatureReading.class);
       }

       @Override
       public boolean isEndOfStream(TemperatureReading nextElement) {
           return false;
       }

       @Override
       public TypeInformation<TemperatureReading> getProducedType() {
           return TypeInformation.of(TemperatureReading.class);
       }
   }

}