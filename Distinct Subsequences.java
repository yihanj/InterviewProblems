public class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
    
        //int [][] dp = new int[n+1][m+1];
        int [] precomb = new int[m+1];
        int [] comb = new int[m+1];
    
        for(int i=0; i<=m; ++i){
            //dp[0][i] = 1;
            precomb[i] = 1;
        }
        for(int j=1; j<=n; ++j){
            for(int i=1; i<=m; ++i){
                if(t.charAt(j-1) != s.charAt(i-1)){
                    //dp[j][i] = dp[j][i-1];
                    comb[i] = comb[i-1];
                }else{
                    //dp[j][i] = dp[j][i-1] + dp[j-1][i-1];
                    comb[i] = comb[i-1] + precomb[i-1];
                }
            }   
            for(int k=0; k<=m; ++k){
                precomb[k] = comb[k];
            }
        }
    
        return precomb[m];        
    }
}
