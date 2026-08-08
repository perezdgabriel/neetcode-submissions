class Solution:
    len_delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + self.len_delimiter + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            len_str = ''
            while s[i] != self.len_delimiter:
                len_str += s[i]
                i += 1
            length = int(len_str)
            res.append(s[i + 1 : i + 1 + length])
            i += length + 1
        return res

        