# O(N) line sweep, since input is guaranteed to be years 1950 - 2050
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for birth, death in logs:
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        population = 0
        max_population = 0
        year = 0

        for idx, count in enumerate(years):
            population += count

            if population > max_population:
                max_population = population
                year = 1950 + idx
        return year


# O(NlogN) line sweep
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth, death in logs:
            events.append((birth, 1))
            events.append((death, 0))
        events.sort(reverse=True)

        best = [0, 0]
        population = 0
        while events:
            year = events[-1][0]
            while events and events[-1][0] == year:
                year, event = events.pop()
                if event:
                    population += 1
                else:
                    population -= 1
            if population > best[0]:
                best = [population, year]
        return best[1]
