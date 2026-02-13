class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0

        while left < len(nums):
            right = left + 1
            while right < len(nums):
                if nums[right] == nums[left]:
                    if (right * left) % k == 0:
                        count += 1
                right += 1
            left += 1

        return count
