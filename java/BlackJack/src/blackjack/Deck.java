/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package blackjack;

/**
 *
 * @author shriamin
 */
public class Deck {

    //private Card card;
    public static enum Test {TEST1, TEST2}

    public boolean testAssert()
    {
        System.out.println("testing asserts...");
        return false;
    }

    public Deck(){
        Card[] x;
        x = new Card[52];
        for(int i = 0; i < 52; ++i){
            x[i] = new Card();

            System.out.println(i + ". suit value:" + x[i].getSuit());
            System.out.println(i + ". rank value:" + x[i].getRank());
    }
    }

}
