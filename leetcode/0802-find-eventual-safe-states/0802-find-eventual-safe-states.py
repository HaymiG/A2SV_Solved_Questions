class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        q = deque()
        safe = [] 
        out =[0] * n
        revers = defaultdict(list)

        for u in range(n):
            out[u] = len(graph[u])
            for v in graph[u]:
                revers[v].append(u)
        
        for i in range(n) :
            if out[i] == 0 :
                q.append(i)
        while q :
            node = q.pop()
            safe.append(node)

            for neb in revers[node]:
                out[neb] -= 1
                if out[neb] == 0 :
                    q.append(neb)
        safe.sort()
        return safe


    

        
        



        
        