def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
            continue
        if not stack:
            return False
        if char == ')':
            if stack.pop() != '(':
                return False
        if char == ']':
            if stack.pop() != '[':
                return False
        if char == '}':
            if stack.pop() != '{':
                return False
    if stack:
        return False
    return True

print(isValid("()[]{}"))
