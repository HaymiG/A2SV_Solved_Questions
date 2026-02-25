class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1  
        prev_last = points[0][1] 
         
        for start, end in points[1:]:
            if start > prev_last:
                count += 1
                prev_last = end  
        return count
        