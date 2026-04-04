class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits :
            return
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
            for ch in dic[digits[index]]:
                currstr =currstr + ch
                back(index + 1 , currstr)
                currstr.pop()
        back(0 , "")
        return res