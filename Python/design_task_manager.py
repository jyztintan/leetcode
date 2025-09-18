class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.priority_list = []
        for user, task, priority in tasks:
            self.tasks[task] = (user, priority)
            heappush(self.priority_list, (-priority, -task))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heappush(self.priority_list, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heappush(self.priority_list, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.priority_list:
            priority, task = heappop(self.priority_list)
            priority, task = -priority, -task
            if task in self.tasks and self.tasks[task][1] == priority:
                user, _ = self.tasks[task]
                self.rmv(task)
                return user
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()