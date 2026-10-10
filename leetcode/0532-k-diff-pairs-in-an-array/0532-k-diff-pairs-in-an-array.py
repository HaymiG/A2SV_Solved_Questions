class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0,1
        res = 0
        while j<len(nums):
            if i==j: j+=1
            else:
                if nums[j]-nums[i]<k: j+=1
                elif nums[j]-nums[i]>k: i+=1
                else:
                    res+=1
                    i+=1
                    while i<len(nums) and nums[i]==nums[i-1]:i+=1
                    if j<=i: j = i+1
        return res