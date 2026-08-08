class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in closing:
                if not stack or closing[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0