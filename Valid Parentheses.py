class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        stack = []

        stack.append(s[0])

        for i in range(1, len(s)):

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])

            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]

                if s[i] == ")" and top == "(":
                    stack.pop()
                elif s[i] == "]" and top == "[":
                    stack.pop()
                elif s[i] == "}" and top == "{":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
