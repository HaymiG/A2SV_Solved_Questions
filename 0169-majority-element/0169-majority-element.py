from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for num, freq in count.items():
            if freq > n // 2:
                return num
