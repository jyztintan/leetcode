# Running sum O(N)
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        street = [0] * (n + 1)
        for pos, reach in lights:
            street[max(0, pos - reach)] += 1
            street[min(n, pos + reach + 1)] -= 1

        brightness = 0
        met_req = 0
        for i in range(n):
            brightness += street[i]
            if brightness >= requirement[i]:
                met_req += 1
        return met_req

# Event-based, O(NlogN) for sorting
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        light_events = []
        for pos, reach in lights:
            light_events.append([max(0, pos - reach), 1])
            light_events.append([min(n + 1, pos + reach + 1), 0])

        light_events.sort(reverse=True)
        brightness = 0
        met_req = 0
        for i in range(n):
            while light_events and light_events[-1][0] == i:
                _, event = light_events.pop()
                if event:
                    brightness += 1
                else:
                    brightness -= 1
            if brightness >= requirement[i]:
                met_req += 1
        return met_req
