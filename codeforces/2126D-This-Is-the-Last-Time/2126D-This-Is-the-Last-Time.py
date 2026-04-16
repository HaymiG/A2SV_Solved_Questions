import heapq

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for _ in range(n)]

    casinos.sort()
    heap = []
    i = 0

    while True:
        while i < n and casinos[i][0] <= k:
            l, r, real = casinos[i]
            if k <= r:
                heapq.heappush(heap, -real)
            i += 1

        if not heap:
            break

        best = -heapq.heappop(heap)
        if best <= k:
            break

        k = best

    print(k)