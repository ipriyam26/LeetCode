# Modules Start
from __future__ import division, print_function
import sys
import os
# import time
from io import BytesIO, IOBase
import math
from collections import defaultdict
# Modules End

# Helpers
INT_MAX = 2147483647
INT_MIN = -2147483648
mod = int(1.e9) + 7
# Helpers End

import math
from collections import defaultdict, deque

def bfs(u, graph, d_thr):
    visited = set()
    queue = deque([(u, 0)])
    max_dist = 0

    while queue:
        node, dist = queue.popleft()

        if node not in visited:
            visited.add(node)
            max_dist = max(max_dist, dist)
            if dist < d_thr:
                for neighbor in graph[node]:
                    queue.append((neighbor, dist + 1))

    return visited, max_dist

def find_node_with_max_degree(graph):
    max_degree_node = -1
    max_degree = -1

    for node, neighbors in graph.items():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree
            max_degree_node = node

    return max_degree_node

def find_subset_nodes(graph, n):
    d_thr = math.ceil(math.sqrt(n))
    start_node = find_node_with_max_degree(graph)
    subset_nodes, max_dist = bfs(start_node, graph, d_thr)

    return subset_nodes if max_dist <= d_thr else -1

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = defaultdict(list)
        
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        subset_nodes = find_subset_nodes(graph, n)
        
        if subset_nodes == -1:
            print(-1)
        else:
            print(len(subset_nodes))
            print(*subset_nodes)

# Settings
sys.setrecursionlimit(10000000)
# Settings End

# region fast_io
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion


if __name__ == '__main__':
    main()
