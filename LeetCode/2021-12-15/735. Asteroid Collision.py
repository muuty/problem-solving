class Solution1(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        removed = set()
        remains = [i for i in range(len(asteroids))]
        previous_removed_count = 0
        while True:
            for i in range(len(remains)):
                if i == 0:
                    continue

                left, right = asteroids[remains[i-1]], asteroids[remains[i]]
                if left > 0 and right < 0:
                    if abs(left) >= abs(right):
                        removed.add(remains[i])
                    if abs(left) <= abs(right):
                        removed.add(remains[i-1])

            if len(removed) == previous_removed_count:
                break

            remains = [i for i in range(len(asteroids)) if i not in removed]
            previous_removed_count = len(removed)
        return [asteroids[i] for i in range(len(asteroids)) if i not in removed]


class Solution2(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        plus = []
        minus = []
        for a in asteroids:
            if a > 0:
                plus.append(a)
            else:
                while plus and plus[-1] < abs(a):
                    plus.pop()
                if not plus:
                    minus.append(a)
                elif plus[-1] == abs(a):
                    plus.pop()

        return minus + plus

#print(Solution().asteroidCollision([5,10,-5]))
#print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([10, 2, -5]))
#print(Solution().asteroidCollision([-2, -1, 1, 2]))
