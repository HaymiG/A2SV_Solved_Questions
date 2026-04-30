class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegree = [0] * n
        graph = defaultdict(list)

        for u , v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        q =deque()
        order = []
        for i in range(n):
            if indegree[i] == 0 :
                q.append(i)
        while q :
            node = q.popleft()
            order.append(node)

            for neb in graph[node]:
                indegree[neb] -= 1
                if indegree[neb] == 0 :
                    q.append(neb)
        if len(order) != n :
            return []
        return order
            