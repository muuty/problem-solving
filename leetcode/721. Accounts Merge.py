import collections

class Solution(object):
    def accountsMerge(self, accounts):
        graph = collections.defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                graph[email].add(account[1])
                graph[account[1]].add(email)
        visited = set()
        ans = []
        for email in email_to_name:
            path = []
            if email not in visited:
                stack = [email]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        path.append(node)
                        visited.add(node)
                        next_nodes = graph[node]
                        stack += list(next_nodes)

                ans.append([email_to_name[email]] + sorted(path))
        return ans


print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))