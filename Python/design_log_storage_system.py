class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.logs, (timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        def get_prefix(s, granularity):
            time = s.split(":")
            match granularity:
                case "Year":
                    match = time[:1]
                case "Month":
                    match = time[:2]
                case "Day":
                    match = time[:3]
                case "Hour":
                    match = time[:4]
                case "Minute":
                    match = time[:5]
                case "Second":
                    match = time
            return ":".join(match)

        prefix = get_prefix(start, granularity)
        ptr = bisect.bisect_left(self.logs, (start, -1)) - 1
        resp = []
        while ptr >= 0 and self.logs[ptr][0].startswith(prefix):
            resp.append(self.logs[ptr][1])
            ptr -= 1
        resp.reverse()

        ptr = bisect.bisect_left(self.logs, (start, -1))

        while ptr < len(self.logs) and self.logs[ptr][0] < end:
            resp.append(self.logs[ptr][1])
            ptr += 1

        prefix = get_prefix(end, granularity)
        while ptr < len(self.logs) and self.logs[ptr][0].startswith(prefix):
            resp.append(self.logs[ptr][1])
            ptr += 1
        return resp

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
