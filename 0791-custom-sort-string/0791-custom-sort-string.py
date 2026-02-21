class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []
        
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]    
        for key , freq in count.items():
            result.append(key * freq)
        return "".join(result) 
                
                
          


        