
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        ##First version
        total_run = 0
        counts = collections.defaultdict(int)
        total_count = 0

        for task in tasks:
            counts[task] += 1
            total_count += 1

        if n == 0:
            return total_count

        only_counts = []
        for key in counts:
            only_counts.append(counts[key])
        only_counts.sort(reverse=True)
        max_tasks = only_counts.count(only_counts[0])

        first_run = (only_counts[0]) * (n+1)
        if first_run > total_count:
            first_run = first_run - (n+1) + max_tasks

        remain_run = max([(total_count - first_run),0])
        print(first_run , remain_run)
        if remain_run % n:
            remain_run = remain_run // n + 1
        else:
            remain_run = remain_run // n
        return first_run + remain_run
        


print(Solution().leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))
print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))