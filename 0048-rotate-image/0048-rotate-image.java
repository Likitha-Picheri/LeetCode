class Solution {
    public void rotate(int[][] matrix) {
        int t=matrix.length;
        int j=0;
        for(int i=0;i<t;i++){
            while(i>j){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
                j++;
            }

            j=0;
        }
        for(int i=0;i<t;i++){
            for(int k=0;k<t/2;k++){
            int temp=matrix[i][k];
            matrix[i][k]=matrix[i][t-1-k];
            matrix[i][t-1-k]=temp;
        }
        }


        
    }
}