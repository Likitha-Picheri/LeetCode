class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int y=piles.length;
        int t=y/3;
        int sum1=0;
        int iterate=y-2;
        while(t>0){
           sum1=sum1+piles[iterate];
           iterate=iterate-2;
           t--;
        }
        return sum1;

        
    }
}