package org.main;
import detectors.LocationOutlierFraudDetector;
import detectors.LocationTresholdFraudDetector;
import detectors.ValueTresholdFraudDetector;
import models.Transaction;
import org.apache.flink.api.java.functions.KeySelector;
import org.apache.flink.api.java.tuple.Tuple2;
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

        DataStream<Transaction> sourceStream = transactionsSourceProvider.getSourceStream(env);

        DataStream<Transaction> fraudsEvents = sourceStream
                .keyBy(Transaction::getUserid)
                    .process(new ValueTresholdFraudDetector())
                .union(sourceStream.keyBy(Transaction::getUserid)
                        .process(new LocationOutlierFraudDetector()))
                .union(sourceStream.keyBy(new KeySelector<Transaction, Tuple2<Long,Long>>(){
                    @Override
                    public Tuple2<Long,Long> getKey(Transaction transaction)
                    {
                        return new Tuple2<Long,Long>(transaction.user_id,transaction.card_id);
                    }
                }).process(new LocationTresholdFraudDetector()));

        sinkProvider.sink(fraudsEvents);

        env.execute("Frauds Detector");
    }

}