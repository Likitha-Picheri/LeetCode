class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        if(k<=numOnes){
            return k;
        }
        else if((numOnes+numZeros)>=k){
           return numOnes;
        }
        else{
            return  2*numOnes-k+numZeros;
        }
    }
}