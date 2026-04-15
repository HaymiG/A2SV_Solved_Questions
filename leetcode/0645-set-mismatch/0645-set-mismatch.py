class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)

        duplicate = -1
        missing = -1

        for key,freq in count.items():
            if freq == 2:
                duplicate = key
        for i in range(1 , n + 1):
            if i not in count:
                missing = i
        return [duplicate , missing]

        