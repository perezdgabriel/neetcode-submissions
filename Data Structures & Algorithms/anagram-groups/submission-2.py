from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for string in strs:
            ss = "".join(sorted(string))
            ht[ss] = ht[ss] + [string]
        
        return [sub for sub in ht.values()]
