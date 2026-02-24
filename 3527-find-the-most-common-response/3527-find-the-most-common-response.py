class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        my_dict = defaultdict(int)

        for i in responses:
            unique = set(i)
            for r in unique:
                my_dict[r] += 1
        max_count = 0
        answer = " "

        for key, value in my_dict.items():
            if value > max_count or (value == max_count and key < answer):
                answer = key 
                max_count = value
        return answer