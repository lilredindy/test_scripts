import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class crushMap {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        //List<Long> ab = new ArrayList<Long>();
        //long ab[] = new long[N];
        HashMap<Integer, Long> ab = new HashMap<Integer, Long>();

        //for (int i = 0; i < N; ++i){
            //ab.add((Long)(long)0);
            //ab[i] = 0;

        //}

        
        while (M-- > 0){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int k = sc.nextInt();
        
            for (int i = a; i <= b; ++i){
                //long sum = ab.get(i - 1) + k;
                //ab.set(i-1, sum); 
                
                //long sum = ab[i-1] +k;
                //ab[i-1] = sum; 
                
                if (!ab.containsKey(i))
                    ab.put(i, (long)0);

                long sum = ab.get(i) + k;
                ab.put(i, sum);
                //System.out.println(ab);
            }
         }
        
        //long max = Collections.max(ab);
        long max =0;
        
        /*
        for (int i = 0; i < N; ++i){
            if (ab[i] > max)
                max = ab[i];   
        }*/


        for (Map.Entry<Integer, Long> entry: ab.entrySet()){
            long value = entry.getValue();
            if (value > max)
                max = value;
        }

        
        System.out.println(max);
      
    }
}