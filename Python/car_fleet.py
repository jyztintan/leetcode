class Solution(object):
    def carFleet(self, target, position, speed):
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = [(target - car[0])/car[1] for car in cars]
        ans, max_time = 0, -1
        for fleet in fleets:
            if fleet > max_time:
                ans += 1
                max_time = fleet
        return ans



# sol = Solution()
# position = [6, 8]
# speed = [3, 2]
# print(sol.carFleet(10, position, speed))
# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]
# print(sol.carFleet(target, position, speed))
# target = 10
# position = [8,3,7,4,6,5]
# speed = [4,4,4,4,4,4]
# print(sol.carFleet(target, position, speed))
# target = 100
# position = [0,2,4]
# speed = [4,2,1]
# print(sol.carFleet(target, position, speed))
