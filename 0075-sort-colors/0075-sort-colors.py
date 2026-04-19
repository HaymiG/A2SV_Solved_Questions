class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for num in nums:
            count[num]+=1
        index = 0
        for color in range(3):
            for i in range(count[color]):
                nums[index] = color
                index += 1
        return nums
                