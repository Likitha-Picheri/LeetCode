class Solution {
    public int minOperations(int[] nums) {
        int min1=0;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]>=nums[i+1]){
                min1=nums[i]-nums[i+1]+min1+1;
                nums[i+1]=nums[i]+1;
            }
        }
        return min1;
    }
}