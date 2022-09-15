arr = [4,5,9,6,2,3]
stack = []
result = []
i =len(arr)-1
while i>=0:
    if not stack:
        result.append(-1)
    elif stack[-1][1] > arr[i]:
        result.append(stack[-1][0]+1)
    else:
        while stack and stack[-1][1]<arr[i]:
            stack.pop()
        if not stack:
            result.append(-1)
        
    