from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        my_dict = defaultdict(int)
        my_dict2 = defaultdict(int)

        for ch in word1:
            my_dict[ch] += 1
        for ch in word2:
            my_dict2[ch] += 1

        if set(my_dict.keys()) != set(my_dict2.keys()):
            return False

        return sorted(my_dict.values()) == sorted(my_dict2.values())