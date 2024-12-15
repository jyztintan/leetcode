from collections import defaultdict
from typing import List


class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        self.parents[self.find(u)] = self.find(v)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ufds = UFDS(len(accounts))

        email_owner = {}
        for idx, (owner, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_owner:
                    ufds.union(email_owner[email], idx)
                email_owner[email] = idx

        merged = defaultdict(list)
        for email, owner in email_owner.items():
            merged[ufds.find(owner)].append(email)

        res = []
        for idx, emails in merged.items():
            owner = accounts[idx][0]
            res.append([owner] + sorted(emails))
        return res
