package providers.config;

public class KafkaConfig {
    public final String SourceTopic;
    public final String SinkTopic;
    public final String BootstrapServer;

    public KafkaConfig()
    {
        SourceTopic = "Transactions";
        SinkTopic = "Frauds";
        BootstrapServer="localhost:9092";
    }
}
