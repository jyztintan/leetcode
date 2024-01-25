def generate_parenthesis(n):
    
    stack = []
    res = []

    def generate_answer(open, close):
        if open == close == n:
            res.append("".join(stack))
            return None
        
        if open < n:
            stack.append("(")
            generate_answer(open + 1, close)
            stack.pop()

        if close < open:
            stack.append(")")
            generate_answer(open, close + 1)
            stack.pop()
        
    generate_answer(0,0)
    return res


        


print(generate_parenthesis(1))
print(generate_parenthesis(2))
print(generate_parenthesis(3))
print(generate_parenthesis(4))
