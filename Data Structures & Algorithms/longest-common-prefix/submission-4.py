class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        letter_index = 0
        end = False
        while not end:
            candidate = ''
            all_match = True
            for word in strs:
                if len(word) <= letter_index + 1:
                    end = True

                if len(word) <= letter_index:
                    all_match = False
                    break

                if candidate == '':
                    candidate = word[letter_index]
                elif word[letter_index] != candidate:
                    all_match = False
                    break

            if all_match:
                prefix += candidate
            elif letter_index == 0:
                break
            letter_index += 1

        return prefix