class ICIMSTest {
  public static void main(String[] args) {
    
    
    int [][] A = {{3,1,9,5},
                  {6,5,7,5},
                  {2,2,10,5},
                  {5,4,9,4},
                  {3,3,10,5}};
    System.out.println(solution(A));
  }
  
 
  
   public static int solution(int[][] A) {
        // write your code in Java SE 8
        int count = 0;
        for (int i = 1; i < A.length -1; ++i){
            for (int j = 1; j < A[0].length -1; ++j){
                System.out.println(String.format("i:%s j:%s A[i][j]:%s", i,j,A[i][j]));
                if (A[i][j] < A[i][j-1] & A[i][j] < A[i][j+1]) //local min in row
                    if (A[i][j] > A[i-1][j] & A[i][j] > A[i+1][j]) //local max in col
                        ++count;
                if (A[i][j] > A[i][j-1] & A[i][j] > A[i][j+1]) //local max in row
                    if (A[i][j] < A[i-1][j] & A[i][j] < A[i+1][j]) //local min in col
                        ++count;
            }
        }
        return count;
    }
  
}
