class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        child = [0] * k
        self.min_f = float('inf')
        
        def backtracking(idx):
            if idx == len(cookies):
                self.min_f = min(self.min_f , max(child))
                return
            if max(child) >= self.min_f:
                return
                
            for i in range(k):
                child[i] +=  cookies[idx]
                backtracking(idx + 1)
                child[i] -=  cookies[idx]

                
        backtracking(0)
        return self.min_f


        