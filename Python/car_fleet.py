def car_fleet(target, position, speed):
    cars = []
    for i in range(len(speed)):
        cars.append([position[i], speed[i]])
    cars.sort(key = lambda x:x[0], reverse = True)
    timing = list(map(lambda car: (target - car[0])/car[1], cars))
    count, max_time = 1, timing[0]
    for time in timing:
        if time <= max_time:
            continue
        count += 1
        max_time = time
    return count

# Recommended tutorial from NeetCode but my solution is faster :D
# def car_fleet(target, position, speed):
#     pairs = [[pos, spd] for pos, spd in zip(position, speed)]
#     stack = []
#     for pair in sorted(pairs)[::-1]:
#         stack.append((target - pair[0])/pair[1])
#         if len(stack) >= 2 and stack[-1] <= stack[-2]:
#             stack.pop()
#     return len(stack)


target = 12
position = [10,8,0,5,3] 
speed = [2,4,1,1,3]
print(car_fleet(target, position, speed))
target = 10
position = [8,3,7,4,6,5]
speed = [4,4,4,4,4,4]
print(car_fleet(target, position, speed))
target = 100
position = [0,2,4]
speed = [4,2,1]
print(car_fleet(target, position, speed))
