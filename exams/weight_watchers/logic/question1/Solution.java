//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;

import java.util.*;

class Solution {

    public static void main( String[] args ) {
        System.out.print("Enter your string: ");
        Scanner sc = new Scanner(System.in);  // Reading from System.in
        String s = sc.nextLine();
        reverseEverything(s);

        /*
        System.out.println("Enter your string: ");
        try{

            BufferedReader bufferReader = new BufferedReader(new InputStreamReader(System.in));
            String s = bufferReader.readLine();
            reverseEverything(s);

        }
        catch (IOException e) {

            e.printStackTrace();
        }*/
    }

    private static void reverseEverything(String s){
        String[] words = s.split(" ");

        for (int i = 0; i < words.length/2; ++i){       //reverse the words
            String tmp = words[i];
            words[i] = words[words.length - 1 - i];
            words[words.length - 1 - i] = tmp;
        } //System.out.println(Arrays.toString(words));

        for (int i = 0; i < words.length; ++i){     //reverse chars of each word
            String tmp = "";
            for (int j = words[i].length()-1; j>=0; --j){
                tmp += words[i].charAt(j);
            }
            words[i] = tmp;
        } //System.out.println(Arrays.toString(words));
        
        StringBuilder sb = new StringBuilder();
        for (String word: words){
            sb.append(word).append(" ");
        }  
        System.out.println("The reversed string: " + sb.toString());
    }     
}