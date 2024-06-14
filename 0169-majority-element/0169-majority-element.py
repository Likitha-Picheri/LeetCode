class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        
        return max(zip(dict.values(),dict.keys()))[1]