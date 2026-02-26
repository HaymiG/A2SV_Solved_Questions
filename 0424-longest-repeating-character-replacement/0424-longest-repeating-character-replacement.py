class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        answer = 0
        left = 0
        for i in range(len(s)):
            cur_len = 0
            need = 0
            
            my_dict[s[i]] += 1
            cur_len = i - left + 1
            max_freq = max(my_dict.values())
            need = cur_len - max_freq 
            if need <= k :
                answer += 1
            else :
                my_dict[s[left]] -= 1
                if my_dict[s[left]] == 0:
                    del my_dict[s[left]]
                left += 1
        return answer
            
 

        
        
    


        