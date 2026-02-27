
n ,s = map(int, input().split())
arr  = list(map(int, input().split()))
result = 0
left = 0
cur = 0
for right in range(n):
  cur += arr[right]

  while cur > s:
    cur -= arr[left]
    left += 1

  result = max(result , right - left + 1)
print(result)
  




  
  
