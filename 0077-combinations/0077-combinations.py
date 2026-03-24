class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        n = 4, k = 2
        [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]

           '''
        arr = [i for i in range(1 , n + 1)] 
        answer = []
        def backtracking( idx, combination):
            if len(combination) == k :
                answer.append(combination[:]) # same as combination.copy
                return
            if idx == len(arr):
                return
            combination.append(arr[idx])
            backtracking( idx + 1, combination)
            
            combination.pop()
            backtracking( idx + 1, combination)

        backtracking(0 , [])
        return answer

        