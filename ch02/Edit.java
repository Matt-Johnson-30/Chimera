import java.lang.reflect.Field;

class Edit
{
    public static void main(String[] args)
    {
        Ship c = new Ship(10,10);
        Field[] fields = Ship.class.getDeclaredFields();

        try
        {
            fields[6].setAccessible(true);
            fields[7].set(c, 10000);
        } catch (Exception e) {}
    }
}
