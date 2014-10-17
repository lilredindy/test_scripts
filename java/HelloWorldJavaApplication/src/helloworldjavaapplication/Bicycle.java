package helloworldjavaapplication;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author shriamin
 */

public class Bicycle {
    public int cadence;
    public int gear;
    public int speed;
    // add an instance variable for the object ID
    private int id;
    // add a class variable for the
    // number of Bicycle objects instantiated
    private static int numberOfBicycles = 45;
    private int serverPort;

    public void Bicycle(Bicycle bike)
    {
        this.cadence = bike.cadence;
        this.gear = bike.gear;
        this.speed = bike.speed;
        System.out.println("bike constructor with bike param works?");
    }

    public void BicycleNotConstructor(Bicycle bike)
    {
        this.cadence = bike.cadence;
        this.gear = bike.gear;
        this.speed = bike.speed;
        System.out.println("bike not constructor with bike param works");
    }

    void setServerPort(String value) throws NumberFormatException {
        System.out.println(value);
    serverPort = Integer.parseInt(value);
    }

    /*
    void setServerPort2(String value) throws ConfigurationException {
        try {
            serverPort = Integer.parseInt(value);
        } catch (NumberFormatException e) {
            throw new ConfigurationException("Port " + value + " is not valid.");
        }
    }*/

    public static int getNumBicycles(){
    
        return numberOfBicycles;
    }

    public void foo(Dog d) {
     d = new Dog("Bob");
}

       public void foo2(Dog d) {
         d.setName("Fifi");
    }

    public void foo3(Dog d) {
    d.setName("Max");     // AAA
      d = new Dog("Fifi");  // BBB
    d.setName("Rowlf");   // CCC
}
    
    public boolean foundSubString(String strToSearch, String strToMatch){

        boolean foundIt = false;
        int len1 = strToSearch.length();
        System.out.println("len1:" + len1);
        int len2 = strToMatch.length();
        System.out.println("len2:" + len2);

        int check = 0;

        for(int i = 0; i <= (len1 - len2); ++i){
            System.out.println("i:" + i);
            for (int j = 0; j < len2; ++j){
                System.out.println("j:" + j);
                if (strToSearch.charAt(i + j) == strToMatch.charAt(j)){
                    ++check;
                    if (check == len2)
                        return foundIt = true;
                    else
                        continue;
                }
                else{
                    foundIt = false;
                    break;
                }
            }

        }
           return foundIt;
    }
    
    public boolean equals(Object o){
       
        return (this == o);
    }
    
} //class
