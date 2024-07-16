class Solution {
    public int maximizeSum(int[] nums, int k) {
        int t=Arrays.stream(nums).max().getAsInt();
        return ((k*t) +(k-1)*(k)/2);
        
    }
}