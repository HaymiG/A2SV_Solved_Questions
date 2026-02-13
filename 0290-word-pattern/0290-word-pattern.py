class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split(" ")
        if len(pattern) != len(words):
            return False
        new = defaultdict(int)
        used = set()
        # print(words ,  pattern)
        for i in range(len(pattern)):
            if pattern[i] in new:
                if words[i]!= new[pattern[i]]:
                    return False
            else :
                if words[i] in used:
                    return False
                else :
                    new[pattern[i]] = words[i]
            used.add(words[i])

            # elif 
            #     new[pattern[i]] = words[i]  

        return True

            
          
            