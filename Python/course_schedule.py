from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        in_degree = [0] * numCourses
        adj_list = defaultdict(list)
        # Process edges
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1

        # Topological sort
        take_now = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                take_now.append(course)

        taken = 0
        while take_now:
            course = take_now.pop()
            taken += 1
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    take_now.append(next_course)
        return taken == numCourses
