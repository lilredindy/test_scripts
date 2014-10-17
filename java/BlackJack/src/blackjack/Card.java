/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package blackjack;

/**
 *
 * @author shriamin
 */

public class Card {

    private final int suit;
    private final int rank;

    private final int JOKER = 0;

    private final int SPADES = 1;
    private final int DIAMONDS = 2;
    private final int HEARTS = 3;
    private final int CLUBS = 4;

    private final int ACE = 1;
    private final int TWO = 2;
    private final int THREE = 3;
    private final int FOUR = 4;
    private final int FIVE = 5;
    private final int SIX = 6;
    private final int SEVEN = 7;
    private final int EIGHT = 8;
    private final int NINE = 9;
    private final int JACK = 10;
    private final int QUEEN = 11;
    private final int KING = 12;

    public Card(){
    this.rank = JOKER;
    this.suit = JOKER;
    }

    public Card(int suit, int rank){
        this.suit = suit;
        this.rank = rank;
    }

    public int getRank(){return this.rank;}
    public int getSuit(){return this.suit;}

}
