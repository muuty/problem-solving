class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                #stack[-1]에 해당하는 애가 지금 height보다 크면 더 유지 불가능
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
            print(stack)
        height.pop()
        return ans


#print(Solution().largestRectangleArea([2,1,5,6,2,3]))
#print(Solution().largestRectangleArea([2,4]))
print(Solution().largestRectangleArea([2,1,2]))