class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        v = list(c.values())

        mx = max(v)
        mn = min(v)

        a = v.copy()
        a.remove(mx)
        if mx - 1 != 0:
            a.append(mx - 1)
        if len(set(a)) == 1:
            return True
        
        b = v.copy()
        b.remove(mn)
        if mn - 1 != 0:
            b.append(mn - 1)
        if len(set(b)) == 1:
            return True
        return False