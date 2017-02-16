import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class brackets {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            String s = in.next();

            String result = "";

            if (s.length() % 2 != 0){
                result = "NO";
                break;     
            }
            
               
            char[] arr = s.toCharArray();
            Stack<Character> st = new Stack<Character>();
            
            st.push(arr[0]);
            for (int i = 1; i < arr.length; ++i){

                if (st.isEmpty()){
                    st.push(arr[i]);         
                    continue;
                }

                Character p = st.peek(); 
            
            
                if (arr[i] == '}' && p == '{')
                    st.pop();
                else if (arr[i] == ']' && p == '[')
                    st.pop();
                else if (arr[i] == ')' && p == '(')
                    st.pop();
                else if (arr[i] == ']' || arr[i] == '}' || arr[i] == ')'){
                    result = "NO";
                    break;   
                }
                else 
                    st.push(arr[i]);          
             }
        
            if (st.isEmpty())
                result = "YES";
            
            System.out.println(result);
        
        }
    }
}