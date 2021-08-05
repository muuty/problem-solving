class Solution(object):
    def merge(self, intervals):

        result = []
        intervals.sort(key=lambda x: x[0])
        x1 = x2 = -1
        for interval in intervals:
            if x1 == -1:
                x1, x2 = interval
                continue

            y1, y2 = interval

            if x2 < y1:
                result.append([x1, x2])
                x1, x2 = y1, y2
            else:
                x2 = max(x2, y2)

        result.append([x1, x2])
        return result
