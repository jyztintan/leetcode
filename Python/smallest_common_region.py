class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        adj_list = {}
        for regioning in regions:
            bigger = regioning[0]
            for smaller in regioning[1:]:
                adj_list[smaller] = bigger

        increasing_region1 = [region1]
        while region1 in adj_list:
            increasing_region1.append(adj_list[region1])
            region1 = adj_list[region1]
        increasing_region2 = [region2]
        while region2 in adj_list:
            increasing_region2.append(adj_list[region2])
            region2 = adj_list[region2]

        smallest_common = -1
        limit = min(len(increasing_region1), len(increasing_region2))
        while increasing_region1[smallest_common] == increasing_region2[smallest_common]:
            if smallest_common == - limit:
                return increasing_region1[smallest_common]
            smallest_common -= 1
        return increasing_region1[smallest_common + 1]

regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
region1 = "Quebec"
region2 = "Canada"
print(Solution().findSmallestRegion(regions, region1, region2))
