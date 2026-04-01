class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [ ]
        used = [False] * n
        def backtracking(path):
            if len(path) == n:
                ans.append(path[:])
            
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(path)
                path.pop()
                used[i]= False
        backtracking([])
        return ans
            

            
        
        