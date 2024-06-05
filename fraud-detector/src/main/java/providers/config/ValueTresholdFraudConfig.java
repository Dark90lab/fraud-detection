package providers.config;

import models.Range;

import java.io.Serializable;

public class ValueTresholdFraudConfig implements Serializable {
    public final double minValueAmount;
    public final double largeValueAmount;
    public final Range fraudsTimeRange;

    public ValueTresholdFraudConfig() throws  Exception
    {
        minValueAmount = 1.0d;
        largeValueAmount = 500.0d;
        fraudsTimeRange = new Range("1,5");
    }
}
