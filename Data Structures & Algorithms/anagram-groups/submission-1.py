class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            ss = "".join(sorted(s))
            anagrams[ss] = anagrams[ss] + [s] if ss in anagrams else [s]

        return list(anagrams.values())
