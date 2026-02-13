import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

   
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (1 if s[i] == 'R' else -1)

    
    first = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first = i
            break

    if first == -1 or first > k:
        print(0)
        continue

    
    cycle = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle = i
            break

    if cycle == -1:
        print(1)
    else:
        print(1 + (k - first) // cycle)
