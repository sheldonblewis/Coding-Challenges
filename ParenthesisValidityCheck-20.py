class Solution:
    def isValid(self, s: str) -> bool:
        stack = "."

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack += s[i]
            elif s[i] == ')':
                if stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    return False
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack = stack[:-1]
                else:
                    return False
        
        if stack == ".":
            return True
        return False
