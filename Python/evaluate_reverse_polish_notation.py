class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char.isdigit() or char[1:].isdigit():
                stack.append(int(char))
                continue
            operand2, operand1 = stack.pop(), stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            else:
                stack.append(int(operand1 / operand2))
        return stack[0]
