class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        answer = list(dominoes)
        right_forces = [None] * len(dominoes)
        left_forces = [None] * len(dominoes)
        force_count = 0
        current_direction = None
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                force_count = 1
                current_direction = 'R'
            elif dominoes[i] == '.' and current_direction == 'R':
                right_forces[i] = force_count
                force_count += 1
            elif dominoes[i] == 'L':
                current_direction = 'L'

        force_count = 0
        current_direction = 'None'
        for i in range(len(dominoes)):
            if dominoes[len(dominoes) - 1 - i] == 'L':
                force_count = 1
                current_direction = 'L'
            elif dominoes[len(dominoes) - 1 - i] == '.' and current_direction == 'L':
                left_forces[len(dominoes) - 1 - i] = force_count
                force_count += 1
            elif dominoes[len(dominoes) - 1 - i] == 'R':
                current_direction = 'R'

        for i in range(len(dominoes)):
            if answer[i] == '.':
                if not left_forces[i] and right_forces[i]:
                    answer[i] = 'R'
                elif not right_forces[i] and left_forces[i]:
                    answer[i] = 'L'
                elif right_forces[i] > left_forces[i]:
                    answer[i] = 'L'
                elif left_forces[i] > right_forces[i]:
                    answer[i] = 'R'
                else:
                    answer[i] = '.'
        print(left_forces)
        print(right_forces)
        return ''.join(answer)

print(Solution().pushDominoes(".L.R...LR..L.."))