class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result=[]
        def backtrack(subset,indx):
            if len(digits)==indx:
                result.append("".join(subset))
                return
            for ch in dic[digits[indx]]:
                subset.append(ch)
                backtrack(subset,indx+1)
                subset.pop()
        backtrack([],0)
        return result