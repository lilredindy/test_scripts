// Copyright 2016-2017 Karat, Inc.  Please do not distribute or republish.

import java.io.*;
import java.util.*;

/*

Write a function that takes two user’s browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample output:

(user0, user2):
   /four.html
   /six.html
   /seven.html

(user1, user2):
   /two.html
   /three.html
   /four.html
   /six.html

(user0, user3):
   None

(user1, user3):
   /three.html
 */

class Solution {
  
  
  static List<String> user0 = Arrays.asList(
      "/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html" );
  static List<String> user1 = Arrays.asList(
      "/one.html", "/two.html", "/three.html", "/four.html", "/six.html");
  static List<String> user2 = Arrays.asList(
      "/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html");
  static List<String> user3 = Arrays.asList("/three.html", "/eight.html");

  // Your function here
  
  
  
  public static List<String> compare(List<String> userA, List<String> userB){
    
    List<String> L = new ArrayList<String>();
    /*
    
    if (userA.length > userB.length){
      //loop with A
    }
    else
      //loop with B
      */
      
      int count = 0;
      int max_count = 0;
      //int len = userA.length;
      for (int i = 0; i < userA.size(); ++i){
       
        for (int j = 0; j < userB.size(); ++j){

          if (userA.get(i) == userB.get(j)){
            ++count;
            L.add(userA.get(i));
            
          }
          else{
            //if (count > max_count) 
          }
          

        
        }
        
                  
        
      }
      
     /* 
    for (String s : userA){
     
      userA.get(s
    }*/
    
    return L; 
  
  }
  
  
  
  
  public static void main(String[] args) {
    
    
   List<String> user0 = Arrays.asList(
      "/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html" );
   List<String> user1 = Arrays.asList(
      "/one.html", "/two.html", "/three.html", "/four.html", "/six.html");
    
  List<String> result = compare(user0, user1);
    
    System.out.println(result);

  }
}


