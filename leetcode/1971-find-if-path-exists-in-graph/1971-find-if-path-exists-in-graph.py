class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # using recursion 
        graph = defaultdict(list)
        visited = set()
        stack = [source]

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # using stack
        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            if cur in visited:
                continue
            visited.add(cur)
            for neb in graph[cur]:
                if neb not in visited:
                    stack.append(neb)
        return False
       


        
        
        # def dfs(graph , node , visited , destination):
        #     if node == destination :
        #         return True
            
        #     visited.add(node)
        #     for neb in graph[node]:
        #         if neb not in visited :
        #             visited.add(neb)
        #             if dfs(graph , neb , visited ,destination):
        #                 return True
        #     return False 
        # return dfs(graph , source , visited , destination)

            