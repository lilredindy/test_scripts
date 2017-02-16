import java.util.*;

class stack{

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
            Character start = '\0';
            int start_index = -1;
            Character end = '\0';
            int end_index = -1;

            while (result.isEmpty()) {

              for (int i = 0; i < L.size(); ++i){

                Character c = L.get(i);

                //System.out.println(i);

                if ((c == '(') || (c == '{') || (c =='[')) {

                  if (i == L.size() - 1) 
                    result = "false";

                  start = L.get(i);
                  start_index = i;
                  end_index = -1;
                  continue; //for
                }

                if ((c == ')') || (c == '}') || (c == ']')) {
                  end = L.get(i);
                  end_index = i;
                }

                //System.out.println("L: " + Arrays.toString(L.toArray()));

                if ((start_index == -1) || (end_index == -1)){
                  result = "false";
                  break; //for 
                }
                else {
                  L.remove(end_index);
                  L.remove(start_index);
                   
                  //System.out.println("L: " + Arrays.toString(L.toArray()));

                  if (L.isEmpty())
                    result = "true";
                
                  start_index = -1;
                  end_index = -1;
                  break; //for
                } 

              } //for  
            } //while  
            System.out.println(result);
      } //hasNext
    } //main

}

