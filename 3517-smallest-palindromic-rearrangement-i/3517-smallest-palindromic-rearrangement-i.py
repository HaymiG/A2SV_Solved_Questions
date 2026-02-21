class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        count = dict(sorted(c.items()))
        first = []
        middle = ""
        if len(s) == 1:
            return s
        print(count, " coiunt")
        for ch in sorted(count.keys()):
            first.append(ch * (count[ch] // 2))
            if count[ch] % 2 != 0:
                middle = ch
            
           
           
        f = ''.join(first)
        return f + middle + f[::-1]
            


                
            




        