class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        result = []
        max_len = [0]
        def is_unique(string):
            if len(set(string)) < len(string):
                return False
            return True

        def get_next_string(current_string, i, max_len):
            if not is_unique(current_string):
                return

            if i == len(arr):
                if len(current_string) > max_len[0]:
                    max_len[0] = len(current_string)
                return

            get_next_string(current_string + arr[i], i+1, max_len)
            get_next_string(current_string, i+1, max_len)

        get_next_string("", 0, max_len)

        return max_len[0]




print(Solution().maxLength(["cha","r","act","ers"]))