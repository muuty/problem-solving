import bisect
from collections import defaultdict


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        will_left = defaultdict(int)  # (will_left[_to] = num_passenger
        arrivals = list()
        trips.sort(key=lambda x: x[1])

        current = 0
        for num_passenger, _from, _to in trips:
            left_until = 0
            for i in range(len(arrivals)):
                if -1 * arrivals[len(arrivals) - 1 - i] <= _from:
                    left_until = i + 1
                    continue
                else:
                    break

            for i in range(left_until):
                arrival = arrivals[-1]
                current -= will_left[-1 * arrival]
                will_left[-1 * arrival] = 0
                arrivals.pop()

            current += num_passenger
            if current > capacity:
                return False

            will_left[_to] += num_passenger
            bisect.insort(arrivals, -1 * _to)

        return True


#print(Solution().carPooling([[2,1,5],[3,3,7]], 4))
#print(Solution().carPooling([[2,1,5],[3,3,7]], 5))
#print(Solution().carPooling([[3,2,8],[4,4,6],[10,8,9]], 11))
print(Solution().carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]], 12))

