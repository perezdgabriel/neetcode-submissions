class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 0
        li = 0
        window = set()

        for ri, char in enumerate(s):
            while char in window:
                window.remove(s[li])
                li += 1
            window.add(char)
            res = max(res, ri - li + 1)
            print(f'char:{char} - li:{li} - ri:{ri} - res:{res} - window:{window}')
        
        return res

            