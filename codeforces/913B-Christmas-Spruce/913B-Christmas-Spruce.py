n = int(input())

children = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    p = int(input())
    children[p].append(i)

is_leaf = [False] * (n + 1)

for i in range(1, n + 1):
    if len(children[i]) == 0:
        is_leaf[i] = True

for i in range(1, n + 1):
    if len(children[i]) > 0:  # non-leaf
        leaf_count = 0
        for ch in children[i]:
            if is_leaf[ch]:
                leaf_count += 1

        if leaf_count < 3:
            print("No")
            exit()

print("Yes")