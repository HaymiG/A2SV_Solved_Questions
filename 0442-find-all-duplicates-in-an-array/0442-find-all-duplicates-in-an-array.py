class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for key,freq in count.items():
            if freq > 1:
                result.append(key)
        return result