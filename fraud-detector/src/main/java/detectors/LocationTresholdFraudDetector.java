package detectors;

import models.Transaction;
import org.apache.flink.api.common.functions.OpenContext;
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;
import providers.config.ConfigProvider;
import providers.config.LocationConfig;

public class LocationTresholdFraudDetector extends KeyedProcessFunction<Tuple2<Long,Long>, Transaction,Transaction> {
    private transient ValueState<Tuple2<Double, Double>> lastLocationState;
    private final LocationConfig config = ConfigProvider.getInstance().locationConfig;
    private transient ValueState<Long> timerState;

    @Override
    public void open(OpenContext openContext) {
        ValueStateDescriptor<Tuple2<Double, Double>> locationDescriptor =
                new ValueStateDescriptor<>("lastLocation", Types.TUPLE(Types.DOUBLE, Types.DOUBLE));
        ValueStateDescriptor<Long> timerDescriptor =
                new ValueStateDescriptor<>(
                        "timerState",
                        Types.LONG
                );
        timerState = getRuntimeContext().getState(timerDescriptor);
        lastLocationState = getRuntimeContext().getState(locationDescriptor);
    }

    @Override
    public void processElement(Transaction transaction, KeyedProcessFunction<Tuple2<Long,Long>, Transaction, Transaction>.Context context, Collector<Transaction> collector) throws Exception {
        Tuple2<Double, Double> lastLocation = lastLocationState.value();
        Long timerTimestamp = timerState.value();
        Tuple2<Double, Double> currentLocation = new Tuple2<>(transaction.location.lat, transaction.location.lon);
        long currentProcessingTime = context.timerService().currentProcessingTime();

        if(lastLocation!= null && timerTimestamp != null)
        {
            if (Math.abs(currentLocation.f0 - lastLocation.f0) > config.maxRadiusDeviation || Math.abs(currentLocation.f1 - lastLocation.f1) > config.maxRadiusDeviation)
            {
                collector.collect(transaction);
            }
        }

        lastLocationState.update(currentLocation);

        // Set a timer if not already set
        if (timerTimestamp == null) {
            long timer = currentProcessingTime + config.locationTimeTreshold*1000;
            context.timerService().registerProcessingTimeTimer(timer);
            timerState.update(timer);
        }
    }

    @Override
    public void onTimer(long timestamp, OnTimerContext ctx, Collector<Transaction> out) {
        // Clear the state when the timer triggers
        timerState.clear();
        lastLocationState.clear();
    }

}
