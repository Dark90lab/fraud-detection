package providers.config;

import models.Range;

import java.io.Serializable;

public class ValueTresholdFraudConfig implements Serializable {
    public final float minValueAmount;
    public final float largeValueAmount;
    public final Range fraudsTimeRange;

    public ValueTresholdFraudConfig() throws  Exception
    {
        minValueAmount = 1.0f;
        largeValueAmount = 5.0f;
        fraudsTimeRange = new Range("0,0.5");
    }
}
