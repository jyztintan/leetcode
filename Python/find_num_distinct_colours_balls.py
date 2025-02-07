class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Ball to colour
        coloured = {}
        # Colour to num balls
        used_colours = {}

        output = []
        for ball, colour in queries:
            if ball in coloured:
                original = coloured[ball]
                used_colours[original] -= 1
                if used_colours[original] == 0:
                    del used_colours[original]
            used_colours[colour] = used_colours.get(colour, 0) + 1
            coloured[ball] = colour
            output.append(len(used_colours))

        return output
