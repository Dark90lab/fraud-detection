package detectors;

import models.Transaction;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;
import providers.config.ConfigProvider;
import providers.config.LocationConfig;

public class LocationOutlierFraudDetector extends KeyedProcessFunction<Long, Transaction,Transaction> {
    private final LocationConfig config = ConfigProvider.getInstance().locationConfig;

    @Override
    public void processElement(Transaction transaction, KeyedProcessFunction<Long, Transaction, Transaction>.Context context, Collector<Transaction> collector) throws Exception {

        boolean isInBox = config.IsLocationInGeoBoundingBox(transaction.location.lat, transaction.location.lon);
            if(!isInBox)
            {
                collector.collect(transaction);
            }
    }
}
