package mappers;

import com.fasterxml.jackson.databind.ObjectMapper;
import models.Transaction;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.typeinfo.TypeInformation;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

public  class TransactionDeserializationSchema implements DeserializationSchema<Transaction> {

    @Override
    public Transaction deserialize(byte[] message) throws IOException {
        String jsonString = new String(message, StandardCharsets.UTF_8);

        ObjectMapper mapper = new ObjectMapper();
        return mapper.readValue(jsonString, Transaction.class);
    }

    @Override
    public boolean isEndOfStream(Transaction nextElement) {
        return false;
    }

    @Override
    public TypeInformation<Transaction> getProducedType() {
        return TypeInformation.of(Transaction.class);
    }
}
