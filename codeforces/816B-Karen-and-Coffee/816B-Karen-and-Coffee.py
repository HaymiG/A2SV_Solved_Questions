import sys

def solve():
    
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    k = int(input[1])
    q = int(input[2])
    
    MAX_VAL = 200000

    diff = [0] * (MAX_VAL + 2)
    
    pointer = 3

    for _ in range(n):
        l = int(input[pointer])
        r = int(input[pointer + 1])
        diff[l] += 1
        diff[r + 1] -= 1
        pointer += 2
        
    
    current_recipes = 0
    admissible = [0] * (MAX_VAL + 2)
    for i in range(1, MAX_VAL + 1):
        current_recipes += diff[i]
        if current_recipes >= k:
            admissible[i] = 1
            
    
    
    prefix_sum = [0] * (MAX_VAL + 2)
    for i in range(1, MAX_VAL + 1):
        prefix_sum[i] = prefix_sum[i-1] + admissible[i]
        

    results = []
    for _ in range(q):
        a = int(input[pointer])
        b = int(input[pointer + 1])
        # The number of admissible temps in [a, b] is P[b] - P[a-1]
        results.append(str(prefix_sum[b] - prefix_sum[a - 1]))
        pointer += 2
        

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()