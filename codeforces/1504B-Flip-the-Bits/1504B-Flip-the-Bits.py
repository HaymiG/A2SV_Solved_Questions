t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())

    balance = [0]*(n+1)

    for i in range(n):
        balance[i+1] = balance[i] + (1 if a[i]=='1' else -1)

    flip = 0
    ok = True

    for i in range(n-1, -1, -1):

        cur = a[i]
        if flip:
            cur = '1' if cur=='0' else '0'

        if cur == b[i]:
            continue

        if balance[i+1] != 0:
            ok = False
            break

        flip ^= 1

    print("YES" if ok else "NO")