class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        d = {i:set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            d[prereq].add(course)

        visited = [0] * numCourses

        order = []
        def dfs(course):

            # If it is still pending, then this is an invalid course mapping
            if visited[course] == 1:
                return False

            # If this course has been completed, then it is valid
            if visited[course] == 2:
                return True

            visited[course] = 1
            for next in d[course]:
                if not dfs(next):
                    return False

            visited[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

# prerequisites = [[1,0],[0,2],[2,3]]
# print(Solution().findOrder(4, prerequisites))
