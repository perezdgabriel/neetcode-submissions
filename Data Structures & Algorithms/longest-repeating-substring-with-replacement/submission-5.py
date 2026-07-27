class Solution:
    def most_frequent(self, cset: dict[str, int]) -> int:
        return max(count for count in cset.values())

    def characterReplacement(self, s: str, k: int) -> int:
        L, res = 0, 0
        char_count = {}
        mfc = 0

        for R, char in enumerate(s):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            mfc = max(mfc, char_count[char])
            while R - L + 1 - mfc > k:
                char_count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)
        
        return res