class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        new = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]

            while new and word[:len(new)] != new:
                new = new[:-1]

        return new
