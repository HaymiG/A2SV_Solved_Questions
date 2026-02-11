class Solution(object):
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):   
            complement = target - nums[i]
            if complement in nums_hash:
                return [nums_hash[complement], i]
            nums_hash[nums[i]] = i
