class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)

        frequencies=Counter(nums)
        print(frequencies)
        sorted_nums=sorted(nums,key=lambda x:(freq_map[x],-x))

        
        return sorted_nums
        