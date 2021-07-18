class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(point):
            return point[0] * point[0] + point[1] * point[1]

        points.sort(key=lambda x: distance(x))

