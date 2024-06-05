package providers.config;
import models.Range;

import java.io.Serializable;

public class LocationConfig implements Serializable {
    public final Range longitude;
    public final Range latitude;
    public final double maxRadiusDeviation;
    public final long locationTimeTreshold;

    public LocationConfig() throws Exception {
        latitude = new Range("24.396308,49.384358");
        longitude = new Range("-125.0,-66.93457");
        maxRadiusDeviation = 5d;
        locationTimeTreshold = 5;
    }

    public boolean IsLocationInGeoBoundingBox(double lat, double lon)
    {
        return lat >= latitude.from && lat <= latitude.to && lon >= longitude.from && lon <= longitude.to;
    }
}
