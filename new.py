# Python3 program for implementation of
# SSTF disk scheduling
 
# Calculates difference of each
# track number with the head position
def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)
     
# find unaccessed track which is
# at minimum distance from head
def findMin(diff):
 
    index = -1
    minimum = 999999999
 
    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index
     
#Shubham Singh(SHUBHAMSINGH10)
