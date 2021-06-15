class Solution(object):
    def maximumSwap(self, num):
        num = str(num)
        firsts = {}
        finals = {}


        for i in range(len(num)):
            if int(num[i]) not in firsts:
                firsts[int(num[i])] = i
            finals[int(num[i])] = i
        reverse_firsts = {firsts[key] : key for key in firsts}


        for position in sorted(reverse_firsts.keys()):
            candidates = [i for i in range(0, 10) if i > int(reverse_firsts[position])
                          and i in finals
                          and finals[i] > position]
            if len(candidates) > 0:
                print(max(candidates))
                swap = max(candidates)
                swap_position = finals[swap]
                return num[:position] + str(swap) + num[position+1:swap_position] + str(reverse_firsts[position]) + num[swap_position+1 : ]


        return int(num)
print(Solution().maximumSwap(98368))
