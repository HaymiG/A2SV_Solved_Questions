class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        gaps = []
        n = len(heights)

        if ladders >= n-1:
            return n-1

        for i in range(1, n):
            if heights[i-1]<heights[i]:
                heightDiff = heights[i]-heights[i-1]
                
                heapq.heappush(gaps, -heightDiff)
                
                bricks -= heightDiff
                if bricks<0:
                    if ladders>0:
                        ladders -= 1
                        bricks -= heapq.heappop(gaps)              
                    else:
                        return i-1

        return n-1
                