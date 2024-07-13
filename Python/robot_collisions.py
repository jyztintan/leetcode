class Robot:
    def __init__(self, pos, health, dir):
        self.pos = pos
        self.health = health
        # True if robot is going right, and False if going left
        self.dir = dir

    def __repr__(self):
        return f"<Robot {self.pos}, HP {self.health}, Dir {'R' if self.dir else 'L'}>"

class Solution:
    def survivedRobotsHealths(self, positions, healths, directions: str):
        robots = []
        for i in range(len(positions)):
            robot = Robot(positions[i], healths[i], directions[i] == "R")
            robots.append(robot)

        robots_copy = robots.copy()
        robots.sort(key=lambda robot:robot.pos)

        st = []
        for robot in robots:
            while st and st[-1].dir == True and robot.dir == False:
                # If the previous robot moving right has higher health,
                # We decrement its health by 1 and destroy the current robot (don't add to stack)
                if st[-1].health > robot.health:
                    st[-1].health -= 1
                    robot.health = 0
                    break

                # If the previous robot has same or lower health than the current
                # If they have the same health, both gets destroyed
                elif st[-1].health == robot.health:
                    st.pop().health = 0
                    robot.health = 0
                    break

                # If the current robot has higher health, we destroy the previous robot
                # Then decrement the current robot's health
                else:
                    st.pop().health = 0
                    robot.health -= 1

            # If robot is still alive, add it to the stack
            if robot.health != 0:
                st.append(robot)

        # We need to return health of robots for those still alive
        # but also in the original ordering that the input robots were given
        ans = []
        for robot in robots_copy:
            if robot.health:
                ans.append(robot.health)
        return ans

# positions = [3,5,2,6]
# healths = [10,10,15,12]
# directions = "RLRL"
# print(Solution().survivedRobotsHealths(positions, healths, directions))

