class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int t=nums.size();
        int i=0,sum=0;
        for(i=0;i<t;i++){
            sum+=nums[i];
        }
        int total_sum= t*(t+1)/2;
        int missing=total_sum-sum;
     return missing;
    }

};