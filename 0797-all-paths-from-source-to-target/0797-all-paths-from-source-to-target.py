class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(a):
            if a[-1] == n - 1:
                res.append(a)
                return      
            for child in graph[a[-1]]:
                dfs(a + [child])
                
        res, n = [], len(graph)            
        dfs([0])
        return res
        