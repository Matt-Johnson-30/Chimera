import java.lang.reflect.Field;

class View
{
        public static void main(String[] args)
        {
                Main m = new Main();
				m.main(null);
                Field[] mFields = Main.class.getDeclaredFields();

				//mFields[2].setAccessible(true);
//				Field g = mFields.class.getDeclaredField("Game");


				for (Field f : mFields)
        		{
            		System.out.print(f);
                	try
                	{
                        f.setAccessible(true);
                        System.out.println((int)f.getClass());
                	} catch (Exception e) {}
        		}
                System.out.println();

        }
}
