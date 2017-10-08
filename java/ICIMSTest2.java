
class ICIMSTest2 {
  public static void main(String[] args) {
    int [] A = {2,1,3,4};
    System.out.println(solution(A));
  }
  
 
    public static int solution(int[] A) {
        // write your code in Java SE 8
        
        int count = 0;        
        int perm_sum = 0;
        int sum = 0;
        for (int P = 0; P < A.length; ++P){
            sum += A[P];     
            perm_sum += (P+1);
            if (sum == perm_sum)
                ++count;   
        }
        return count;
    } 
  
}

