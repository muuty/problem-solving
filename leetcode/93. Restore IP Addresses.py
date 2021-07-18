class Solution(object):
    def restoreIpAddresses(self, s):
        def search(answer, remain_string, index, result):
            # answer = [number, number, number]
            print(answer, index)
            if index > 0 and int(answer[-1]) > 255:
                return

            if remain_string == '':
                if index < 4:
                    return

            if index == 4:
                result.append('.'.join(answer))
                return

            elif index == 3:
                if remain_string == str(int(remain_string)):
                    search(answer + [remain_string], '', index + 1, result)
                return
            else:
                for i in range(1, min(len(remain_string)+1, 4)):
                    if remain_string[0:i] == str(int(remain_string[0:i])):
                        search(answer + [remain_string[0:i]], remain_string[i:], index + 1, result)

        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        search([], s, 0, result)
        return result

print(Solution().restoreIpAddresses("1111"))