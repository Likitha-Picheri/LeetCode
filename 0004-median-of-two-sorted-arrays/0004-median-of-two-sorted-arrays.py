class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t=[]
        while nums1 and nums2:
            if nums1[0]>nums2[0]:
                t.append(nums2.pop(0))
            else:
                t.append(nums1.pop(0))
        if nums1 and not nums2:
            t+=nums1
        else:
            t+=nums2
        print(t)
        x=len(t)
        if x%2==0:
            return (t[x//2-1]+t[x//2])/2
        else:
            return t[x//2]

        