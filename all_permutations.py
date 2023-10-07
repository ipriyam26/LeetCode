from typing import List

arr = [1, 2, 3]

def recurr(current: List, leftover: List):
    if not leftover:
        return [current]  # Make it a list of list

    ans = []
    for i in range(len(leftover)):
        data = leftover[:i] + leftover[i + 1 :]
        result = recurr(current+[leftover[i]], data)
        ans.extend(result)  # extend instead of append

    return ans

print(recurr([], arr))
