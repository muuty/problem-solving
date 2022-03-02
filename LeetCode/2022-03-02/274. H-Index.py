class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        answer = 0
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                answer = i+1
                continue
            break

        return answer

print(Solution().hIndex([3,0,6,1,5]))