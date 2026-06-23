class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ["(", "[", "{"]
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                elif char == "]" and top != "[":
                    return False
                elif char == "}" and top != "{":
                    return False
        
        return True if not stack else False