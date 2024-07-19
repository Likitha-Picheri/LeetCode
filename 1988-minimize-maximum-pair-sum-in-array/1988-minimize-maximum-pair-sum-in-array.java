class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int t=nums.length;
        int max=0;
        for(int i=0;i<t/2;i++){
            if(max<nums[i]+nums[t-i- 1]){
                max=nums[i]+nums[t-i-1];
            }
        }
        return max;

        
    }
}