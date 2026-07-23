class Solution:
    def get_ht(self, string: str) -> Dict[str, int]:
        ht = {}
        for char in string:
            if char in ht:
                ht[char] += 1
            else:
                ht[char] = 1
        return ht

    def isAnagram(self, s: str, t: str) -> bool:
        hts = self.get_ht(s)
        htt = self.get_ht(t)
        
        if len(hts) != len(htt):
            return False

        for char, value in hts.items():
            val_t = htt.get(char, -1)
            if val_t != value:
                return False

        return True
