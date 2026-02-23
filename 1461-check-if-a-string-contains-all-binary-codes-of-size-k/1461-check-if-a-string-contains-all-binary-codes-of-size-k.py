class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sub = set()
        for i in range(len(s) - k + 1):
            a = s[i : i + k]
            sub.add(a)
       
        return len(sub) == 2 ** k
        
    #    good job it passed 
    # do we can minimize three line?????
    # okay 
    # what about now????
    # great thats is it..
    # can i submit it ?