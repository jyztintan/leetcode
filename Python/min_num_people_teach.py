class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # for each user, we find the most lacking language
        # we need to first identify the lacking friendships -> cannot communicate
        languages = list(map(set, languages))
        need = []
        for u, v in friendships:
            u -= 1
            v -= 1
            if languages[u].intersection(languages[v]):
                continue
            need.append(u)
            need.append(v)

        best = float('inf')
        for lang in range(1, n + 1):
            count = 0
            for u in need:
                if lang not in languages[u]:
                    count += 1
                    languages[u].add(lang)
            best = min(best, count)
        return best

        # we find the demand for someone to learn a language
