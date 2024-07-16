class Solution {
    public int maximizeSum(int[] nums, int k) {
        Arrays.sort(nums);
        int t=nums[nums.length-1];
        return ((k*t) +(k-1)*(k)/2);
        
    }
}