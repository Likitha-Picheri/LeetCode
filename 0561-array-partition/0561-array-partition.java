class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int maximum_sum=0;
        for(int i=0;i<nums.length;i=i+2){
            maximum_sum=maximum_sum+nums[i];
        }
        return maximum_sum;
    }
}
