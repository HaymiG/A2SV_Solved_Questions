class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for n in reversed(nums):
            if n == 0:
                answer.append(0)
            while n:
                answer.append(n % 10)
                n //= 10
        return list(reversed(answer))
