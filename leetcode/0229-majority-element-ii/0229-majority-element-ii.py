class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n =len(nums)
        least =  n // 3 
        result = []
        count = Counter(nums)
        for val , fre in count.items():
            if fre > least:
                result.append(val)
        return result
        