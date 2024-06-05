package models;

import java.io.Serializable;

public class Range implements Serializable {
    public final double from;
    public final double to;

    public Range(String range) throws Exception {
        var splitRange = range.split(",");

        if(splitRange.length != 2)
            throw new Exception(String.format("Range must be defined by two float numbers separated by ',' delimiter, given: %s",range));
        from = Double.parseDouble(splitRange[0]);
        to = Double.parseDouble(splitRange[1]);
    }
}
