class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s :
            if ch == "*":
                stack.pop()
                continue
            stack.append(ch)
        result = "".join(stack)
        return result
            
        