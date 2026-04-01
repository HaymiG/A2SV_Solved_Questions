class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        def helper(left , right):
            if left > right:
                return -1
            mid = (left + right ) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1 , right)
            else :
                return helper(left , mid - 1)
        res = helper(left , right)
        return res



        