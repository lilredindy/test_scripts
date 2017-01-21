import java.util.*;

class stack_fail{
   
   public static void main(String []argh)
   {
      Scanner sc = new Scanner(System.in);
      
      while (sc.hasNext()) {
          String input=sc.next();
          //System.out.println(input);
          char[] chars = input.toCharArray();
          List<Character> L = new ArrayList<Character>();
          for (int i = 0; i < chars.length; ++i)
              L.add(chars[i]);
          
          //System.out.print(chars[i]);
          //System.out.println(Arrays.toString(parts));
          //List<char> charlist = Arrays.asList(chars);

          /*
          for (Character c: L)
              System.out.print(c);
          System.out.println();
          */
          
          String result = "true";
          while (true){

          	//System.out.println("hell");
        
             
              if (L.size() == 0)
                  break;
              if (L.size() % 2 != 0){
                  result = "false";
                  break;  
              }

              
              if (L.get(0) == '('){
                  if (L.get(L.size() -1) == ')'){
                      L.remove(L.size() -1);
                      L.remove(0);
                      continue;
                  } 
                  if (L.get(1) == ')'){
                      L.remove(1);
                      L.remove(0);
                      continue;
                  }
                  
                  result = "false"; 
                  break; 
              }

              if (L.get(0) == '['){
                  if (L.get(L.size() -1) == ']'){
                      L.remove(L.size() -1);
                      L.remove(0);
                      continue;
                  } 
                  if (L.get(1) == ']'){
                      L.remove(1);
                      L.remove(0);
                      continue;
                  }
                  
                  result = "false"; 
                  break; 
              }

              if (L.get(0) == '{'){
                  if (L.get(L.size() -1) == '}'){
                      L.remove(L.size() -1);
                      L.remove(0);
                      continue;
                  } 
                  if (L.get(1) == '}'){
                      L.remove(1);
                      L.remove(0);
                      continue;
                  }
                  
                  result = "false"; 
                  break; 
              }

              result = "false";
              break;
             
          }   //while loop    
          
          System.out.println(result);
          
      }
      
   }
}
