class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtracking(index , path):
            if len(path) >= 2 :
                answer.append(path[:])

            used = set()
            for i in range(index , len(nums)):
                
                    if nums[i] in used:
                        continue
                    if not path or path[-1] <= nums[i]:
                        used.add(nums[i])
                        path.append(nums[i])
                        backtracking(i+ 1,path)
                        path.pop()
                
        backtracking(0 , [])
        return answer 
            

        