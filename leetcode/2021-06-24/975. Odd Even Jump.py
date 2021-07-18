class Solution(object):
    def oddEvenJumps(self, arr):
        n = len(arr)
        next_higher = [0] * n
        next_lower = [0] * n

        stack = []

        # [10, 13, 12, 14, 15] -> [10,0], [12, 2], [13, 1], [14, 3], [15, 4]
        # 어차피 값이 큰 애들 중 가장 작은 애를 골라야 하니까 값으로 미리 정렬
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                # stack[-1]은 stack에 있는 가장 큰 인덱스
                next_higher[stack.pop()] = i
            stack.append(i)


        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)


print(Solution().oddEvenJumps([10,13,12,14,15]))