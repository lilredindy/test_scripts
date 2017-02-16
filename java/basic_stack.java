import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class basic_stack {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
       
        int N = Integer.parseInt(sc.nextLine());
        
        Stack<Integer> st = new Stack<Integer>();
        while (N-- > 0){
            
           // String[] q = sc.nextLine().split(" ");
        	int q = sc.nextInt():
            
            //System.out.println(Arrays.toString(q));
            
            switch(q){
                case 1: // -Push the element x into the stack.
                    int x = sc.nextInt();
                    st.push(x);
                    break;
                case 2: // -Delete the element present at the top of the stack.
                    st.pop();
                    break;      
                case 3: // -Print the maximum element in the stack.
                    Stack<Integer> st_cp = (Stack<Integer>) st.clone();
                    
                    int max = -1;
                    int p = -1;
                    while (!st_cp.isEmpty()){
                        p = (int)st_cp.pop();
                        if (p > max)
                            max = p;
                    }
                    System.out.println(max);
                    break;
                default:
                    break;
            }
        }
    }
}