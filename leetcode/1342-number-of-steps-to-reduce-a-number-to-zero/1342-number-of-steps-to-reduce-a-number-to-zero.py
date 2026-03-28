class Solution:
    def numberOfSteps(self, n: int) -> int:
        def helper(n, step):
            if n == 0 :
                return step
            if n % 2 == 0 :
                return helper(n // 2, step + 1)
            else:
                return helper(n -1  ,step + 1 )
        return helper(n ,0)