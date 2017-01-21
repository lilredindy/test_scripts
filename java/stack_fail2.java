import java.util.*;

class stack_fail2{

  public static Boolean isPalindrome(List<Character> l){

          Boolean result = true;

          while (l.size() > 0){
            
            //System.out.println("isPali: " + Arrays.toString(l.toArray()));

            if (l.get(0) == '('){
              if (l.get(1) == ')'){
                l.remove(1);
                l.remove(0);
                continue;
              }
              if (l.get(l.size() -1) == ')'){
                l.remove(l.size() -1);
                l.remove(0);
                continue;
              } 
             
              result = false; 
              break; 
            }
            else if (l.get(0) == '['){
              if (l.get(1) == ']'){
                l.remove(1);
                l.remove(0);
                continue;
              }
              if (l.get(l.size() -1) == ']'){
                l.remove(l.size() -1);
                l.remove(0);
                continue;
              } 
             
              result = false; 
              break; 
            }
            else if (l.get(0) == '{'){
              if (l.get(1) == '}'){
                l.remove(1);
                l.remove(0);
                continue;
              }
              if (l.get(l.size() -1) == '}'){
                l.remove(l.size() -1);
                l.remove(0);
                continue;
              } 
            }
            else {
              result = false; 
              break;
            }    
          }   

        return result;
   } //isPalindrome



   public static void main(String []argh){
      Scanner sc = new Scanner(System.in);
      
      while (sc.hasNext()) {
          String input=sc.next();
          char[] chars = input.toCharArray();


          List<Character> L = new ArrayList<Character>();
          for (int i = 0; i < chars.length; ++i)
              L.add(chars[i]);



          if (L.size() % 2 != 0){
              System.out.println("false");
              continue;
            }


          String result = "";

          while (!L.isEmpty()) {


            Character lBrace = L.get(0);
            Character rBrace = ' ';

            if (lBrace == '(')  
              rBrace = ')';
            else if (lBrace == '{')  
              rBrace = '}';
            else if (lBrace == '[')  
              rBrace = ']';
            else{
              result = "false";
              break; //inner while
            } 

          
            List<Character> subL = new ArrayList<Character>();
            int counter = 0;

            for (int i = 1; i < L.size(); ++i){
              
              if (L.get(i) == lBrace){
                ++counter;
              }
              
              if (L.get(i) == rBrace){
                if (counter == 0){
                    
                    for (int j = 0; j <= i; ++j){
                      subL.add(L.get(j));
                    }
                    
                    L.subList(0, i+1).clear();
                    
                    break; //exit for 
                }
                else 
                  --counter;
              }
            
            } //for  

            System.out.println("subL: " + Arrays.toString(subL.toArray()));
            System.out.println("L: " + Arrays.toString(L.toArray()));

            if (subL.isEmpty()){
              result = "false";
              break; //inner while
            }

            if (isPalindrome(subL)){
              result = "true";
              continue;
            }
            else {
              result = "false";
              break; //inner while 
            }

        } // while L.isEmpty 
        System.out.println(result);
      } //hasNext
    } //main

}









