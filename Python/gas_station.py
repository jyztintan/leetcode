class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        best = 0
        net = 0
        total = 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if net < 0:
                net = 0
                best = i + 1

        return best if total >= 0 else -1

