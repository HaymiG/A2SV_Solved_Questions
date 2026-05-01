class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        result = []
        def dfs(n):
            if n in safe:
                return safe[n]
            safe[n] = False
            for neb in graph[n]:
                if not dfs(neb):
                    return False 
            safe[n] = True
            return True


        for n in range(n):
            if dfs(n):
                result.append(n)
        return result
        



        
        