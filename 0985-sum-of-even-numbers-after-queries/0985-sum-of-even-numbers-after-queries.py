class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(queries)):
            index = queries[i][1]
            value = queries[i][0]

            nums[index] += value
            even_sum = 0

            for k in range(len(nums)):
                if nums[k] % 2 == 0:
                    even_sum += nums[k]
            result.append(even_sum)
        return result
        


