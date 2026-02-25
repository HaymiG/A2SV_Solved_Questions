class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        
        for word in strs:
            
           words = tuple(sorted(word))
           groups[words].append(word)
        return  list(groups.values())
        

            
           

        #  for word in words:
        #         common_word = counter(word) 
            # for group in groups:
            #     if Counter(word) == Counter(group[0]):
            #         group.append(word)
            #         break
            # else:
            #     groups.append([word])
        # return groups







        # return List(groups.values()) 
            