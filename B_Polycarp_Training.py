t = int(input())

n = list(map(int , input().split()))
n.sort() 
day = 1
i = 0
while i < t:
  if n[i] >= day:
    day += 1
  i += 1
print(day -1)
  