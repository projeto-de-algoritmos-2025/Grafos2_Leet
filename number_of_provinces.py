# https://leetcode.com/problems/number-of-provinces/
from typing import List


class UnionFind:

    def __init__(self, n: int):
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [0] * n
        self.num_sets: int = n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1

        self.num_sets -= 1

        return True


class Solution:

    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        union_find = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j] == 1:
                    union_find.union(i, j)

        return union_find.num_sets
