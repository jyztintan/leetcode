def daily_temperature(temperatures):
    result = [0 for x in temperatures]
    stack = [] #store a pair : [index, temp]

    for index,temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            stack_index, stack_temp = stack.pop()
            result[stack_index] = index - stack_index
        stack.append([index, temp])
    return result



# temperatures = [73,74,75,71,69,72,76,73]
# print(daily_temperature(temperatures))
# temperatures = [30,40,50,60]
# print(daily_temperature(temperatures))
# temperatures = [30,60,90]
# print(daily_temperature(temperatures))
