import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class CadreTest2 {
  
  public static void main(String[] args) {
    
    CadreTest2 ct = new CadreTest2();

    int[][] rect = {{0,0,0,0,0},
                      {0,0,0,0,0},
                      {0,1,1,1,0},
                      {0,1,1,1,0},
                      {0,0,0,0,0}};

   // System.out.println(ct.returnPointsOfRect(matrix));
    for (Point p : ct.pointsOfRect(rect))
      System.out.println(String.format("x:%d y:%d" , p.getX(),p.getY()));
  }
  
  
  public List<Point> pointsOfRect(int[][] matrix){
    
    List<Point> L = new ArrayList<Point>();
    
    for (int i = 0; i < matrix[0].length; ++i) { //row
      for (int j = 0; j < matrix.length; ++j){ //col
        
        if (matrix[i][j] == 1){ 
          Point p = new Point(i,j);
          //Point p = new Point();
          //p.setX(i);
          //p.setY(j);
          L.add(p);
        }
      }
    }
    return L;
  }

  public class Point {
    private int x;
    private int y;
    
    public Point(){}

    public Point(int x, int y){
      this.x =x;
      this.y =y;
    }

    public void setX(int x){
      this.x = x;
    }
    public int getX(){
      return this.x;
    }
    public void setY(int y){
      this.y = y;
    }
    public int getY(){
      return this.y;
    }
  }
  
}
