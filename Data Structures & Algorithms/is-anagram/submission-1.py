from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        for char, cs in count_s.items():
            ct = count_t.get(char, -1)
            if cs != ct:
                return False
        
        return True

        