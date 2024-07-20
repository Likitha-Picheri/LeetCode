class Solution {
    public int diagonalSum(int[][] mat) {
        int len=mat.length;
        int sum=0;
        for(int i=0;i<len;i++){
            for(int j=0;j<len;j++){
                if(i==j){
                    sum+=mat[i][i];
                }
                else if((i+j)==len-1){
                    sum+=mat[i][j];
                }
            }
        }
        return sum;
        // for(int i=0;i<len;i++){
        //     sum+=mat[i][i];
        //     System.out.println(sum);
        
        // }
        // int j=0;

        // for(int i=len-1;i>=0;i--){
        //     sum+=mat[j][i];
        //     j++;

        // }
        // if(len%2==0){
        //     return sum;
        // }
        // else{
        //     len=len/2;
        //     return sum-mat[len][len];
        // }
        
    }
}