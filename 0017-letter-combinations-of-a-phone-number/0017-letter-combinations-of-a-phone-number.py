class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits :
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
        def back(index , currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return
            for ch in dic[digits[index]]:
                
                back(index + 1 , currstr + ch)
                
        back(0 , "")
        return res