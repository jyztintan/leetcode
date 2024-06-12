def decodeString(s: str) -> str:
    res, num = "", 0
    stack = []
    for char in s:
        if char.isdigit():
            num = num*10 + int(char)
        elif char == "[":
            stack.append(res)
            stack.append(num)
            res = ""
            num = 0
        elif char == "]":
            multiplier = stack.pop()
            substring = stack.pop()
            res = substring + multiplier * res
        else:
            res += char
    return res


# s1 = "3[a]2[bc]"
# s2 = "1[mi]2[ssi]1[pi]"
#
# print(decodeString(s1))
# print(decodeString(s2))