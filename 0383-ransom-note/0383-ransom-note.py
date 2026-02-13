class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] > 0:
                mag_count[ch] -= 1
            else:
                return False
        return True