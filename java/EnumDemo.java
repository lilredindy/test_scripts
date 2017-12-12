enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY,
    THURSDAY, FRIDAY, SATURDAY 
}

public class EnumDemo {

 public static void main(String[] args) {
  
  // Using values method
   Day[] allDays = Day.values();
   for(Day day : allDays){
    System.out.println(day);
   }
   // Using valueOf() method
   Day day = Day.valueOf("TUESDAY");
   System.out.println("Day - " + day);  
 }
}