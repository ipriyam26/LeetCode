from typing import List


def takeFirst(element):
    return element[0]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=takeFirst)
        new_arr = []
        i = 0
        while i < len(intervals):
            element = intervals[i]
            if not new_arr:
                new_arr.append(element)
                i += 1
                continue
            if element[0] <= new_arr[-1][1]:
                new_arr[-1] = [
                    min(new_arr[-1][0], element[0]),
                    max(new_arr[-1][1], element[1]),
                ]
            else:
                new_arr.append(element)
            i += 1
        return new_arr

arr = [[1,4],[4,5]]
print(Solution().merge(arr))
