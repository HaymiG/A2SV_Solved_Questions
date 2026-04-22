class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        # visited = set()
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [source]
        visited = set([source])
        while stack :
            node = stack.pop()
            if node == destination :
                return True
            for neb in graph[node]:
                if neb not in visited:
                    stack.append(neb)
                    visited.add(neb)
        return False

        # def dfs(node , visited):
        #     if node == destination :
        #         return True
        #     visited.add(node)
        #     for neighbor in graph[node]:
        #         if neighbor not in visited :
        #             if dfs(neighbor , visited):
        #                 return True
        #     return False
        # return dfs(source , visited)
        