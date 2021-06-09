class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left = 1
        right = max(piles)
        answer = 0
        while left <= right:

            middle = (left + right) // 2
            req_hour = sum([((pile-1) // middle) + 1 for pile in piles])

            if req_hour > h:
                left = middle + 1
            else:
                answer = middle
                right = middle - 1

        return answer

#print("answer ", Solution().minEatingSpeed([3,6,7,11], 8))
print("answer ", Solution().minEatingSpeed([30,11,23,4,20], 5))
#print("answer ", Solution().minEatingSpeed([30,11,23,4,20], 6))