import java.lang.reflect.Field;

class View
{
        public static void main(String[] args)
        {
                Main m = new Main();
				m.main(null);
                Field[] mFields = Main.class.getDeclaredFields();

				mFields[2].setAccessible(true);
				Field[] gFields = mFields[2].getClass().getDeclaredFields();

/*
				for (Field f : sFields)
        		{
            		System.out.print(f);
                	try
                	{
                        f.setAccessible(true);
                        System.out.println((int)f.get(gFields[5].getClass()));
                	} catch (Exception e) {}
        		}
                System.out.println();
*/
        }
}
