class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int flag=0;
        int index;
         for(int i=0;i<nums.size()-1 && nums.size()>1;i++){
               if(target<nums[i]){
                     index=0;
                     flag=1;
                     break;
               }
               else if(target>nums[i] && target<=nums[i+1]){
                   index=i+1;
                   flag=1;
                   break;
               }
               else if(target==nums[i] && target<=nums[i+1]){
                   index=i;
                   flag=1;
                   break;
               }

         }
         if(flag==1){
             return index;
         }
         else if(nums.size()==1){
             if(target<=nums[0]){
                 return 0;
             }
             else{
                 return 1;
             }
         }
         else{
             return nums.size();
         }
    }
};