package providers.config;

import java.util.HashMap;
import java.util.Map;

public class ConfigProvider {
    private static final ConfigProvider _instance;

    static {
        try {
            _instance = new ConfigProvider();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private final Map<String, String> envVariables;
    public final KafkaConfig kafkaConfig;
    public final ValueTresholdFraudConfig valueTresholdFraudConfig;
    public final LocationConfig locationConfig;

    private ConfigProvider() throws Exception {
        envVariables = new HashMap<>(System.getenv());
        kafkaConfig = new KafkaConfig();
        valueTresholdFraudConfig = new ValueTresholdFraudConfig();
        locationConfig = new LocationConfig();
    }

    public static ConfigProvider getInstance() {
        return _instance;
    }

    private String getVariable(String key) {
        return envVariables.getOrDefault(key, null);
    }
}

