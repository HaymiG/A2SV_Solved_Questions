class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        com = Counter(nums).most_common()
        result = []
        for i in range(k):
            result.append(com[i][0])
        return result
        