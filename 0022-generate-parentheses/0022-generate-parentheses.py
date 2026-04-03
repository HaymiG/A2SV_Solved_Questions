class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracing(curr , open , close):
            if len(curr)== 2 *n :
                result.append(curr)
                return
            if open < n :
                backtracing(curr + "(" , open +1 , close)
            if close < open :
                backtracing(curr + ")" , open, close + 1)
        backtracing("", 0 , 0)
        return result 