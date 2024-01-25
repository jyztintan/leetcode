import math 
def evalRPN(tokens):
    stack = []
    for char in tokens:
        print(stack)
        if char[-1].isdigit():
            stack.append(char)
            continue
        first = stack.pop()
        second = stack.pop()
        num = eval(second + char + first)
        if type(num) != int:
            if num > 0:
                num = str(math.floor(num))
            else:
                num = str(math.ceil(num))
        stack.append(str(num))
    return int(stack[0])



tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))
tokens = ["4","13","-"]
print(evalRPN(tokens))
tokens =["4","-2","/","2","-3","-","-"]
print(evalRPN(tokens))
