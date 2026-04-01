class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low+ (high - low ) // 2 
            day = 1
            load = 0 
            for i in weights:
                if i + load <= mid:
                    load += i 
                else:
                    day += 1
                    load = i
            if day > days:
                low = mid + 1
            else :
                high = mid -1
        return low
            




        