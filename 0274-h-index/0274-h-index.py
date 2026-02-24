class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        sum = 0
        for i in range(n):
            sum += citations[i]
        return sum // n
            
        

        