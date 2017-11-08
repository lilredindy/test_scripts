import java.util.*;


public class SystemProperty {
    public static void main(String []args) {
		//Properties prop = new Properties();
		
		System.out.println(System.getProperty("java.class.path"));  

		String s1 = "java";
		String s2 = s1;
		s1 = "c++";
		System.out.println(s1);
		System.out.println(s2);
   }
}

