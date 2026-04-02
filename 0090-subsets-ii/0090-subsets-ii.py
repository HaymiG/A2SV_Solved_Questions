class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        def backtracking(index , subset ):
            if index >= len(nums):
                answer.append(subset[:])
                return 
            #choosing the number 
            subset.append(nums[index])
            backtracking(index + 1 , subset)
            # not choosing it 
            subset.pop()
            while index + 1<len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtracking(index + 1 , subset)
        backtracking(0 , [])
        return answer       

        