class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        adj_list = defaultdict(set)
        in_degrees = [0] * numCourses
        for pre, course in prerequisites:
            in_degrees[course] += 1
            adj_list[pre].add(course)

        q = deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                q.append(course)

        # Process prereqs
        prereqs = defaultdict(set)
        while q:
            course = q.popleft()
            for next_course in adj_list[course]:
                prereqs[next_course].add(course)
                prereqs[next_course].update(prereqs[course])
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    q.append(next_course)

        # Process queries
        response = []
        for pre, course in queries:
            response.append(pre in prereqs[course])
        return response
