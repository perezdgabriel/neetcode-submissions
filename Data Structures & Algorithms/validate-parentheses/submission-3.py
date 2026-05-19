class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                opened.append(bracket)
            else:
                if len(opened) == 0:
                    return False
                elif bracket == ')' and opened[-1] == '(':
                    opened.pop()
                elif bracket == '}' and opened[-1] == '{':
                    opened.pop()
                elif bracket == ']' and opened[-1] == '[':
                    opened.pop()
                else:
                    return False
        return len(opened) == 0