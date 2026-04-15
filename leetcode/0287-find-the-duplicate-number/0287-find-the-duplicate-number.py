class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_n = -1
        for key,freq in count.items():
            if freq > 1:
                return key
            
        
        