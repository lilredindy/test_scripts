import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class equal_stacks {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n1 = in.nextInt();
        int n2 = in.nextInt();
        int n3 = in.nextInt();
        //int h1[] = new int[n1];
        List<Integer> l1 = new ArrayList<Integer>();
        for(int h1_i=0; h1_i < n1; h1_i++){
           l1.add(in.nextInt());
           // h1[h1_i] = in.nextInt();
        }
        //int h2[] = new int[n2];
        List<Integer> l2 = new ArrayList<Integer>();
        for(int h2_i=0; h2_i < n2; h2_i++){
            l2.add(in.nextInt());
            //h2[h2_i] = in.nextInt();
        }
        //int h3[] = new int[n3];
        List<Integer> l3 = new ArrayList<Integer>();
        for(int h3_i=0; h3_i < n3; h3_i++){
            l3.add(in.nextInt());
          //  h3[h3_i] = in.nextInt();
        }
        
     
       //List<Integer> l1 = Arrays.asList(h1); //Returns a fixed-size list backed by the specified array.
       //List<Integer> l2 = Arrays.asList(h2);
       //List<Integer> l3 = Arrays.asList(h3);
        
       Collections.reverse(l1); //passing a pointer
       Collections.reverse(l2); //passing a pointer
       Collections.reverse(l3); //passing a pointer

       Stack<Integer> st1 = new Stack<Integer>();
       Stack<Integer> st2 = new Stack<Integer>();
       Stack<Integer> st3 = new Stack<Integer>();

       int s1= 0;
       int s2 = 0;
       int s3 = 0;
       int max = -1;
       int empty_stacks = 0;
       
       List<Integer> matches = new ArrayList<Integer>();
         
        
       while(!(l1.isEmpty() &&  l2.isEmpty() && l3.isEmpty())){
  
                empty_stacks = 0;
           
                if (!l1.isEmpty()){
                    if (max != s1) {
                        st1.push(l1.get(0));
                        l1.remove(0);
                    }
                }
                else if (max != s1)
                    break;

           
                if (!l2.isEmpty()){
                    if (max != s2) {
                        st2.push(l2.get(0));
                        l2.remove(0);
                    }
                }
                else if (max != s2)
                    break;
           
                
                if (!l3.isEmpty()){
                    if (max != s3) {
                        st3.push(l3.get(0));
                        l3.remove(0);
                    }
                }
                else if (max != s3)
                    break;

           
           
           s1 = getSum(st1);
           s2 = getSum(st2);
           s3 = getSum(st3); 
           
           //now check if all v1-v3 are equal
           if (s1 == s2 && s1 == s3 ){
             // System.out.println("maches!");
               matches.add(s1);
              max = -1; //reset max
           }
           else
            max = Math.max(Math.max(s1,s2), s3);

            
               /*
              System.out.println(max);           
              System.out.println(st1);
              System.out.println(l1);
              System.out.println(st2);
              System.out.println(l2);
              System.out.println(st3);
              System.out.println(l3);
               */
 
       } //while     
        
    int big = 0;
    for(Integer m : matches){
        if (m > big)
            big = m;
    }
    
    System.out.println(big);

    } //main
    
    
    
    private static int getSum(Stack<Integer> st){
        
        if (st.isEmpty())
            return -1;
        
        int sum = 0;
        Iterator iter = st.iterator();
        
        while (iter.hasNext()){
            sum += (int)iter.next();
        }
        return sum;
            
    }
  
        
    
}
