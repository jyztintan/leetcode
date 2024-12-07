from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        taken = []
        while take_now:
            course = take_now.pop()
            taken.append(course)
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    take_now.append(next_course)

        if len(taken) != numCourses:
            return []
        return taken
