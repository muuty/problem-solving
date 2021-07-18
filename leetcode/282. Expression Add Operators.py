
class Solution(object):
    def addOperators(self, num, target):
        def dfs(remain, answer, value, last, result):
            if not remain:
                if value == self.target:
                    result.append(answer)
                return

            for i in range(1, len(remain) + 1):
                if i == 1 or (i > 1 and remain[0] != "0"):
                    new = remain[:i]
                    dfs(remain[i:], answer + '+' + new, value + int(new), int(new), result)
                    dfs(remain[i:], answer + '-' + new, value - int(new), -int(new), result)
                    dfs(remain[i:], answer + '*' + new, value - last + last * int(new), last * int(new), result)

        result = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), result)  # this step put first number in the string
        return result


print(len(Solution().addOperators("105", 5)))


