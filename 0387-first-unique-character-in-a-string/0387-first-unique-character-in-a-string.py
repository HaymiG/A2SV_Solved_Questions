class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for ch in s :
            d[ch] +=1
        for k,v in enumerate(s):
            if d[v]== 1:
                return k
        return -1

       

            

              


        