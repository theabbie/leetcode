from sortedcontainers import SortedList

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.users = defaultdict(SortedList)
        self.taskmap = {}
        self.tasks = SortedList()
        for uid, tid, p in tasks:
            self.add(uid, tid, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskmap[taskId] = (userId, priority)
        self.users[userId].add((priority, taskId))
        self.tasks.add((priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.taskmap[taskId]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        userId, priority = self.taskmap[taskId]
        self.users[userId].remove((priority, taskId))
        self.tasks.remove((priority, taskId))
        del self.taskmap[taskId]

    def execTop(self) -> int:
        if len(self.tasks) == 0:
            return -1
        priority, taskId = self.tasks[-1]
        userId, priority = self.taskmap[taskId]
        self.rmv(taskId)
        return userId