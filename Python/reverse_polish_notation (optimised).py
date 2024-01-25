import math 
def evalRPN(tokens):
    stack = []
    for char in tokens:
        print(stack)
        if char[-1].isdigit():
            stack.append(int(char))
            continue
        first = stack.pop()
        second = stack.pop()
        if char == "+":
            stack.append(second + first)
        elif char == '-':
            stack.append(second - first)
        elif char == '*':
            stack.append(second * first)
        else:
            stack.append(int(second/first))
    return stack[0]



tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))
tokens = ["4","13","-"]
print(evalRPN(tokens))
tokens =["4","-2","/","2","-3","-","-"]
print(evalRPN(tokens))
