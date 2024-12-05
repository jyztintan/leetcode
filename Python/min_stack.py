class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st:
            self.min_st.append(val)
        else:
            self.min_st.append(min(val, self.getMin()))

    def pop(self) -> None:
        self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
