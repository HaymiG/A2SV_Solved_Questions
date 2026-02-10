class Solution:
    def checkEqual(self, a, b) -> bool:
        a_new = {}
        b_new = {}
    
        for i in range(len(a)):
            if a[i] in a_new:
                a_new[a[i]]+=1
            else:
                a_new[a[i]] = 1
                
        for j in range(len(b)):
            if b[j] in b_new:
                b_new[b[j]]+=1
            else :
                b_new[b[j]]= 1
        
        d = (a_new == b_new)
        return d