class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_set = set()
        for i in nums :
            my_set.add(i)
        for i in range(len(nums)+1):
            if i not in my_set:
                return i
        
        