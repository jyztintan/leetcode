def groupAnagrams(strs):
    d = {}
    for s in strs:
        mid = "".join(sorted(s))
        if mid not in d:
            d[mid] = []
        d[s].append(s)
    return d.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
