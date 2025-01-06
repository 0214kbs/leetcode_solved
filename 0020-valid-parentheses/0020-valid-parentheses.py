class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']' : '['
        }

        stack = []
        for val in s:
            if val in ['(','{','[']:
                stack.append(val)
            else:
                if len(stack) < 0:
                    return False
                comp = stack.pop()
                if brackets[val] != comp:
                    return False
        if len(stack) > 0:
            return False
        return True