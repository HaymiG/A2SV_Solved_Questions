class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        out = float("inf")
        for i in range(n+ 1):
            if i not in nums:

                out = i
        return out
        