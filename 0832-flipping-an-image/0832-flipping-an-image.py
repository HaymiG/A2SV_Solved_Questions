class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            left = 0 
            right = n - 1
            while left <= right :
                r =  row[right]
                l = row[left]
                row[left] = 1 - r
                row[right] = 1 - l
                left += 1
                right -= 1
        return image

        
        


        