n ,s = map(int, input().split())
arr  = list(map(int, input().split()))
answer = 0
left = 0
sum = 0
for right in range(n):
  sum += arr[right]
  while sum >= s:
    answer += n - right
    sum -= arr[left]
    left += 1
print (answer)