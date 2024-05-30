package mappers;

import com.fasterxml.jackson.databind.ObjectMapper;
import models.Transaction;
import org.apache.flink.api.common.serialization.SerializationSchema;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TransactionSerializationSchema implements SerializationSchema<Transaction> {
    private static final ObjectMapper objectMapper = new ObjectMapper();
    private static final Logger LOG = LoggerFactory.getLogger(TransactionSerializationSchema.class);

    @Override
    public byte[] serialize(Transaction transaction)
    {
        try {
            return objectMapper.writeValueAsBytes(transaction);
        } catch(Exception e)
        {
            LOG.error(e.getMessage());
            return null;
        }
    };
}
