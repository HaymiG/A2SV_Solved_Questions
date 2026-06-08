class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        current_sum = 0
        while numbers[left] + numbers[right] != target :
            current_sum = numbers[left] + numbers[right]
            if current_sum < target :
                left += 1
            else :
                right -= 1
        return [ left+ 1 , right + 1] 
            
        