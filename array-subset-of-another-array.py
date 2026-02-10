#User function Template for python3
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
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
            else:
                b_new[b[j]]= 1
            
        for key in b_new:
            if key not in a_new or b_new[key]>a_new[key]:
                return False
        return True