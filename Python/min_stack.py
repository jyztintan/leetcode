class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val):
        self.st.append([val, min(val, self.getMin())])

    def pop(self):
        self.st.pop()

    def top(self) :
        return self.st[-1][0]

    def getMin(self):

        # We need this guard clause because when we push elements getMin() is also called
        if self.st:
            return self.st[-1][1]
        return float("inf")
