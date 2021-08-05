class Solution(object):
    def intervalIntersection(self, firstList, secondList):

        n1, n2 = len(firstList), len(secondList)
        i, j = 0, 0
        output = []
        while i < n1 and j < n2:
            x1, x2 = firstList[i]
            y1, y2 = secondList[j]
            if not (y2 < x1 or x2 < y1):
                output.append([max(x1, y1), min(x2, y2)])


            if x2 < y2:
                i += 1
            else:
                j += 1

        return output