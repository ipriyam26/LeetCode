from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.id = []
        self.size = []

        for i in range(size):
            self.id.append(i)
            self.size.append(1)

    def find(self, x: int):
        root = x
        while root != self.id[root]:
            root = self.id[root]
        while x != root:
            temp = self.id[x]
            self.id[x] = root
            x = temp
        return root

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] > self.size[root_y]:
            self.id[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.id[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def findLargestComponent(self) -> int:
        size_max = 0
        for siz in self.size:
            size_max = max(size_max, siz)
        return size_max


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                continue
            if (num - 1) in hash_map:
                uf.union(i, hash_map.get(num - 1))
            if (num + 1) in hash_map:
                uf.union(i, hash_map.get(num + 1))
            hash_map[num] = i
        return uf.findLargestComponent()
