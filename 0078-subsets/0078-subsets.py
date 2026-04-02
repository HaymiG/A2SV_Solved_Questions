class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtracking(start , path):
            answer.append(path[:]) 
            for i in range(start , len(nums)):

                path.append(nums[i])
                backtracking(i+ 1, path)
                path.pop()

                
        backtracking(0 , [])
        return answer 
        