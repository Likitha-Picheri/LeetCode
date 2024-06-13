class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] reslutarray= new int[2*nums.length];
        for(int i=0; i<nums.length;i++){
            reslutarray[i]=nums[i];
            reslutarray[i+nums.length]=nums[i];
        }
        return reslutarray;
    }
}