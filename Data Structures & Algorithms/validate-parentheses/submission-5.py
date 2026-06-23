class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for char in s:
            if char in closeToOpen:
                if not stack:
                    return False
                if closeToOpen[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False
