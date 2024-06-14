class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3=[]
        for t in arr2:
            y=arr1.count(t)
            for z in range(y):
                arr3.append(t)
                arr1.remove(t)
        arr1.sort()
        while(len(arr1)!=0):
            arr3.append(arr1.pop(0))
        arr1=arr3
        return arr1


        