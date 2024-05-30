package providers.source;

import providers.config.ConfigProvider;

import java.util.Properties;

public class KafkaProperties {
    private static  final String _bootstrapServers = "bootstrap.servers";

    public static Properties getProperties()
    {
        Properties props = new Properties();
        props.setProperty(_bootstrapServers, ConfigProvider.getInstance().kafkaConfig.BootstrapServer);
        props.setProperty("flink.consumer.custom.id", "TransactionsConsumer");

        return props;
    }
}
