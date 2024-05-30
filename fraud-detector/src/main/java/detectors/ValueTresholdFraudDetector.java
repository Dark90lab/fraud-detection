package detectors;
import models.Transaction;
import org.apache.flink.api.common.functions.OpenContext;
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;
import providers.config.ConfigProvider;
import providers.config.ValueTresholdFraudConfig;

public class ValueTresholdFraudDetector extends KeyedProcessFunction<Long, Transaction,Transaction> {
    private transient ValueState<Boolean> flagState;
    private transient ValueState<Long> timerState;
    private final ValueTresholdFraudConfig config = ConfigProvider.getInstance().valueTresholdFraudConfig;

    @Override
    public void open(OpenContext openContext)
    {
        ValueStateDescriptor<Boolean> flagDescriptor = new ValueStateDescriptor<>("flag", Types.BOOLEAN);
        flagState = getRuntimeContext().getState(flagDescriptor);

        ValueStateDescriptor<Long> timerDescriptor = new ValueStateDescriptor<>(
                "timer-state",
                Types.LONG);
        timerState = getRuntimeContext().getState(timerDescriptor);
    }

    @Override
    public void processElement(Transaction transaction, KeyedProcessFunction<Long, Transaction, Transaction>.Context context, Collector<Transaction> collector) throws Exception {
        // Get the current state for the current key
        Boolean lastTransactionWasSmall = flagState.value();

        if(transaction.value < config.minValueAmount)
        {
            flagState.update(true);

            long timer = context.timerService().currentProcessingTime()+ (long)((config.fraudsTimeRange.to - config.fraudsTimeRange.from)*1000);
            context.timerService().registerProcessingTimeTimer(timer);

            timerState.update(timer);
        }

        // Check if the flag is set
        if(lastTransactionWasSmall != null)
        {
            if(transaction.value > config.largeValueAmount)
            {
                collector.collect(transaction);
            }

            cleanUp(context);
        }
    }

    @Override
    public void onTimer(long timestamp, OnTimerContext ctx, Collector<Transaction> out) {
        // remove flag after 1 minute
        timerState.clear();
        flagState.clear();
    }

    private void cleanUp(Context ctx) throws Exception {
        // delete timer
        Long timer = timerState.value();
        ctx.timerService().deleteProcessingTimeTimer(timer);

        // clean up all state
        timerState.clear();
        flagState.clear();
    }
}
