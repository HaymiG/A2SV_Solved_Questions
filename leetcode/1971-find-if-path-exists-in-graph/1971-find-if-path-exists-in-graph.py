class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # using recursion 
        graph = defaultdict(list)
        visited = set()

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(graph , node , visited , destination):
            if node == destination :
                return True
            
            visited.add(node)
            for neb in graph[node]:
                if neb not in visited :
                    visited.add(neb)
                    if dfs(graph , neb , visited ,destination):
                        return True
            return False 
        return dfs(graph , source , visited , destination)

            