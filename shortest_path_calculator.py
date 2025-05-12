# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/
import heapq
import sys
from typing import List, Tuple, Dict

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
        for edge in edges:
            self.adj[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist: Dict[int, int] = {i: sys.maxsize for i in range(self.n)}
        dist[node1] = 0

        pq: List[Tuple[int, int]] = [(0, node1)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if u == node2:
                return current_dist

            if current_dist > dist[u]:
                continue

            if u in self.adj:
                for v, weight in self.adj[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(pq, (dist[v], v))

        return -1