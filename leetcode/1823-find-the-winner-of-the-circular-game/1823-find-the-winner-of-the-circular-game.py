class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n + 1):
            winner = (k + winner) % i
            print(winner + 1)  
        return winner + 1