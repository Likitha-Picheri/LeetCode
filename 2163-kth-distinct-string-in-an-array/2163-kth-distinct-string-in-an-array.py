class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict={}

        for x in arr:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for key in dict.keys():
            if dict[key]==1:
                k-=1
            if k ==0:
                return key
        return ""
            

            
        