/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package blackjack;

/**
 *
 * @author shriamin
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Deck deck1 = new Deck();

         int[][] arrayOfInts = {
            { 32, 87, 3, 589 },
            { 12, 1076, 2000, 8 },
            { 622, 127, 77, 955 },
             {455,232,232,12,34,35,36}

        };

         int len = arrayOfInts.length;

         for (int i = 0; i < len ; ++i){
             for (int j =0; j < arrayOfInts[i].length; ++j){
                 System.out.println(arrayOfInts[i][j]);
             }
         }


         assert deck1.testAssert(); //need to use the -ea runtime flag


         String[][] arrayOfStrings = {
            { "foo", "3gfd", "3f" },
            { "dgfa-3", "s", "3df", "df3" }
        };

         int len2 = arrayOfStrings.length;

         for (int i = 0; i < len2 ; ++i){
             for (int j =0; j < arrayOfStrings[i].length; ++j){
                 System.out.println(arrayOfStrings[i][j]);
             }
         }


    }//main
} //main
