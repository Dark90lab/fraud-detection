package providers.config;

import models.Range;

import java.io.Serializable;

public class ValueTresholdFraudConfig implements Serializable {
    public final double minValueAmount;
    public final double percentageLimitTreshold;
    public final Range fraudsTimeRange;

    public ValueTresholdFraudConfig() throws  Exception
    {
        minValueAmount = 1.0d;
        percentageLimitTreshold = 0.95d;
        fraudsTimeRange = new Range("1,5");
    }
}
