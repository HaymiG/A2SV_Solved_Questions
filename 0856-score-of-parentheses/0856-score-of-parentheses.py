class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for s in s :
            if s == "(":
                stack.append(score)

                score = 0
            else:
                val = stack.pop()
                score = val + max(2 * score , 1)
        return score
        
        