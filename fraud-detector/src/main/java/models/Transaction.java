package models;

public class Transaction {
    public Long id;
    public String type;
    public Long user_id;
    public Long card_id;
    public double value;
    public double timestamp;
    public Location location;

    public Long getUserid()
    {
        return user_id;
    }
}
