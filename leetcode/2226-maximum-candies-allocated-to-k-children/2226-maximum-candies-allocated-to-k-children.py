class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        result = 0 
        while left <= right:
            mid = (right + left) // 2 
            children = sum( pi // mid for pi in candies)
            if children >= k:
                result = mid 
                left = mid + 1
            else:
                right = mid - 1
        return result 

            
        
            
        