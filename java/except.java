import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class except {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int result = 0;
        try {
            int x = sc.nextInt();
            int y = sc.nextInt();
            result = x/y;
            System.out.println(result);
        } 
        catch (InputMismatchException e){
                System.out.println(e);
            }
        catch (ArithmeticException f){
                System.out.println(f);
            }
        finally{
        }
    }
}
