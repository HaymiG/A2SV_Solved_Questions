from collections import Counter
n , m = map(int , input().split())
arr  = list(map(int , input().split()))
brr = list(map(int , input().split()))
counting = Counter(brr)
count = 0 
for i in arr:
  if i in counting:
    count += counting[i]
print (count)
