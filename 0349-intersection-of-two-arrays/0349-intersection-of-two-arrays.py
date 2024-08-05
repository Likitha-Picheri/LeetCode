class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in t:
                t.append(nums1[i])
        return t

        # while nums1 and nums2:
        #     if nums1[0]!=nums2[0]:
        #         t.append(nums2.pop(0))
        #     else:
        #         t.append(nums1.pop(0))
        # if nums1 and not nums2:
        #     t+=nums1
        # elif nums2 and not nums1:
        #     t+=nums2
        # return t

        # k=0
        # j=0
        # while k<len(nums1) and j<len(nums2):
        #     if nums1[k]>nums2[j]:
        #         t.append(nums2[j])
        #         j+=1
        #     elif nums1[k]<nums2[j]:
        #         t.append(nums2[k])
        #         k+=1
        #     else:
        #         t.append(nums2[k])
        #         k+=1
        #         j+=1
        


            

        