class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        n = len(nums) 
        t = n//3
        for k,v in count.items():
            if v > t:
                res.append(k)
        return(res)
        