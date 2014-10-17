/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package helloworldjavaapplication;

/**
 *
 * @author shriamin
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        System.out.println(Bicycle.getNumBicycles());
        //System.out.println(Bicycle.numberOfBicycles);


        String[] students = new String[10];
        String studentName = "Peter Smith";
        students[0] = studentName;
        studentName = "shit";

        System.out.println(studentName);
        String str1 = "foo";
        String str2 = "bar";
        String str3 = null;
        System.out.println(str1);

        System.out.println(str2);


        //Java is always pass-by-value. The difficult thing can be to understand that Java passes objects as references passed by value.
        Bicycle cycle = new Bicycle();
        Dog aDog = new Dog("Max");
        System.out.println(" foo shows:");
        cycle.foo(aDog);
        System.out.println("True if Max:" + aDog.getName().equals("Max"));

        Bicycle cycle2 = new Bicycle();
        Dog aDog2 = new Dog("Max");
        System.out.println(" foo2 shows:");
        cycle2.foo2(aDog2);
        System.out.println("True if Fifi:" + aDog2.getName().equals("Fifi"));

        Bicycle cycle3 = new Bicycle();
        Dog aDog3 = new Dog("Rover");
        System.out.println("foo3 shows:");
        cycle3.foo3(aDog3);
        System.out.println("True is Max:" +aDog3.getName().equals("Max"));

        Bicycle cycle4 = new Bicycle();
        cycle4.setServerPort("5000");


        System.out.println(System.getProperty("java.class.path"));
        System.out.println(System.getProperty("java.version"));


        char[] copyFrom = { 'd', 'e', 'c', 'a', 'f', 'f', 'e',
			    'i', 'n', 'a', 't', 'e', 'd' };
        char[] copyTo = new char[7];
        System.arraycopy(copyFrom, 2, copyTo, 0, 7);
        for (int i=0; i<7; i++)
                System.out.println(copyTo[i]);
        System.out.println(copyTo);


        int[] numbers =
             {1,2,3,4,5,6,7,8,9,10};
         for (int item : numbers) {
             System.out.println("Count is: " + item);
         }

         
         Bicycle myBike = new Bicycle();
         String strToSearch = "foobar";
         String strToMatch = "";
         boolean foundIt = myBike.foundSubString(strToSearch,strToMatch);
         System.out.println("Found substring: " + foundIt);


         Bicycle bike1 = new Bicycle();
         bike1.gear = 5;
         bike1.speed = 4;
         bike1.cadence = 2;
         Bicycle bike2 = new Bicycle();
         bike2.BicycleNotConstructor(bike1);
         //Bicycle bike3 = new Bicycle(bike2);

         String strArr[] = {"fdasf", "dfadsf"};
         int numArr[] = {12,12,23,42112,1212,123};


    }
}

