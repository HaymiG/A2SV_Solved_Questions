
n ,s = map(int, input().split())
arr  = list(map(int, input().split()))
result = float('inf')
left = 0
cur = 0
for right in range(n):
  cur += arr[right]

  while cur >= s:
    result = min(result, right - left + 1)
    cur -= arr[left]
    left += 1

  result = max(result , right - left + 1)
print(result if result != float('inf') else -1)
  




  
  
