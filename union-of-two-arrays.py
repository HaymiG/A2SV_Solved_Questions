class Solution:    
    def findUnion(self, a, b):
        # code here
        a_new = set()
        b_new = set()
        for i in range(len(a)):
            a_new.add(a[i])
        for j in range(len(b)):
            b_new.add(b[j])
        return(a_new|b_new)
            