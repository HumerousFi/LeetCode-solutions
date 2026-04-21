class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth, death in logs:
            events.append((birth, 1))
            events.append((death, -1))
        events.sort()
        population = 0
        max_population = 0
        best_year = 0
        for year, change in events:
            population += change
            if population > max_population:
                max_population = population 
                best_year = year
        return best_year