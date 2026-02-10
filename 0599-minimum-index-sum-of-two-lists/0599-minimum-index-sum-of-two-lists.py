class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashm = {}
        min_sum = float('inf')
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
               if list1[i]==list2[j]:
                 if list1[i] not in hashm:
                    hashm[list1[i]] = []
                 hashm[list1[i]].append( i + j)
        for key,values in hashm.items():
            cur_sum = min(values)
            if cur_sum < min_sum :
                min_sum = cur_sum
                res = [key]
            elif cur_sum == min_sum :
                res.append(key)
        return res
            
            
             

            
            
                
            
                 
            
                
                    
        
        
 

                
                    
        
        