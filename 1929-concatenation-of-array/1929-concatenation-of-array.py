class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num2 = nums
        num2.extend(nums)
        return num2
        