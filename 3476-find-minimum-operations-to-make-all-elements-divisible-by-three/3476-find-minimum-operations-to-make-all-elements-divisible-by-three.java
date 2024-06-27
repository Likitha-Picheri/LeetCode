class Solution {
    public int minimumOperations(int[] nums) {
        int mini=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%3!=0){
                mini+=1;
            }

        }
        return mini;
    }
}