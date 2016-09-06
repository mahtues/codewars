# http://www.codewars.com/kata/the-supermarket-queue

from operator import itemgetter
from heapq import heappush, heappop, nlargest

def test():
    print(queue_time([5,3,4], 1))
    # should return 12
    # because when n=1, the total time is just the sum of the times

    print(queue_time([10,2,3,3], 2))
    # should return 10
    # because here n=2 and the 2nd, 3rd, and 4th people in the 
    # queue finish before the 1st person has finished.

def queue_time(l, n):
    tills = [ 0 for i in range(n) ]

    def imin(l):
        return min(enumerate(l), key=itemgetter(1))[0]

    for t in l:
        tills[imin(tills)] += t

    return max(tills)

def queue_time(l, n):
    tills = [ 0 for i in range(n) ]

    # l * log(n)
    for t in l:
        heappush(tills, t + heappop(tills))

    # n
    return max(tills)

