import heapq


class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        factories = []
        for f, n in factory:
            factories.extend([f] * n)

        robots_num, factories_num = len(robot), len(factories)
        memoize = {}

        def find_min(bot, fact):
            if (bot, fact) in memoize:
                return memoize[(bot, fact)]
            # Managed to fit match all robots to a factory
            if bot == robots_num:
                memoize[(bot, fact)] = 0
            elif fact == factories_num:
                memoize[(bot, fact)] = float('inf')
            else:
                match_curr = abs(robot[bot] - factories[fact]) + find_min(bot + 1, fact + 1)
                skip_curr = find_min(bot, fact + 1)
                memoize[(bot, fact)] = min(match_curr, skip_curr)
            return memoize[(bot, fact)]

        find_min(0, 0)
        return memoize[(0, 0)]

robot = [0, 4, 6]
factory = [[2,2],[6,2]]
print(Solution().minimumTotalDistance(robot, factory))
