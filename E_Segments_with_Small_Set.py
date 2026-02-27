from collections import defaultdict
n ,k = map(int, input().split())
arr  = list(map(int, input().split()))
result = 0
left = 0
new = defaultdict(int)
distnict = 0
for right in range(n):
  if new[arr[right]] == 0:
    new[arr[right]] += 1
    distnict += 1
  else:
    new[arr[right]] += 1
  while distnict > k:
    new[arr[left]] -= 1
    
    if new[arr[left]] == 0:
      distnict -= 1
      del new[arr[left]]
    left += 1
  result += right - left +1
  
print(result)
  




  
  
