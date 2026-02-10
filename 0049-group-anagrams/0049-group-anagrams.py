class Solution(object):
    def groupAnagrams(self, strs):
        groups = [] 
        for word in strs:
            found = False
            for group in groups:
                if Counter(word) == Counter(group[0]):
                    group.append(word)
                    found = True
                    break
            if not found:
                groups.append([word])
        return groups
