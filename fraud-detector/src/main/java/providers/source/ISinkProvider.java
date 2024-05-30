package providers.source;

import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSink;

public interface ISinkProvider<T> {
    DataStreamSink<T> sink(DataStream<T> stream);
}
