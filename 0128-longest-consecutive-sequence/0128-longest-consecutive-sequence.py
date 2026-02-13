class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        nums.sort()
        n = len(nums)

        left = 0
        step = 1
        max_len = 1

        while left < n - 1:
            if nums[left + 1] == nums[left]:
                left += 1               
            elif nums[left + 1] - nums[left] == 1:
                step += 1               
                left += 1
            else:
                max_len = max(max_len, step)
                step = 1                
                left += 1

        return max(max_len, step)
