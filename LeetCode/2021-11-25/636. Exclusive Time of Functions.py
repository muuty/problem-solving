from collections import defaultdict

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        times = defaultdict(int)
        stack = []
        last_time = 0
        last_action = None
        for log in logs:
            function_id, action, time = log.split(":")
            time = int(time)
            if action == "start":
                if stack:
                    duration = time - last_time
                    if last_action == "end":
                        duration -= 1
                    times[stack[-1]] += duration
                stack.append(function_id)

            elif action == "end":
                duration = time - last_time
                if last_action == "start":
                    duration += 1
                times[function_id] += duration
                stack.pop()

            last_time = time
            last_action = action
        answer = [times[str(i)] for i in range(0, n)]
        return answer

print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(Solution().exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
