package providers.source;

import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public interface IDataSourceProvider<T> {
    DataStream<T> getSourceStream(StreamExecutionEnvironment env);
}
