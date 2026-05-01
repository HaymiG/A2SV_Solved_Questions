class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        # visited = set()
        graph = defaultdict(list)
        indegree = [0]*n

        for u , v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        q = deque()
        # order = []
        count  = 0
        
        for i in range(len(indegree)):
            if indegree[i] == 0 :
                q.append(i)

        
        while q :
            node = q.popleft()
            count += 1
            # if node in visited:
            #     continue

            # visited.append(node)
            # order.append(node)

            for neb in graph[node]:
                indegree[neb] -= 1
                if indegree[neb] == 0 :

                    q.append(neb)


        return count == n 






        