class Solution(object):
    def candy(self, ratings):
        blocks = split_continuous_block(ratings)
        blocks = get_minimal_increasing_block(blocks)
        print(blocks)
        blocks = calibrate(blocks, ratings)
        print(blocks)
        return sum([sum(block) for block in blocks])


def calibrate(blocks, ratings):
    current_index =0

    for i in range(len(blocks)):
        if i == 0:
            current_index += len(blocks[i])
            continue
        if blocks[i - 1][0] < blocks[i - 1][-1] and blocks[i][0] > blocks[i][-1] and ratings[current_index-1] > ratings[current_index]:
            if blocks[i - 1][-1] <= blocks[i][0]:
                blocks[i - 1][-1] = blocks[i][0] + 1
        elif blocks[i - 1][0] > blocks[i - 1][-1] and not blocks[i][0] > blocks[i][-1] and ratings[current_index-1] < ratings[current_index]:
            blocks[i] = [i + 2 for i in range(len(blocks[i]))]

        current_index += len(blocks[i])
    return blocks


def split_continuous_block(ratings):
    blocks = []
    block = []
    for rating in ratings:
        if len(block) == 0:
            block.append(rating)

        elif len(block) == 1:
            if block[0] == rating:
                blocks.append(block)
                block = [rating]
            else:
                block.append(rating)

        elif len(block) > 1:
            if (block[-1] - block[-2]) * (rating - block[-1]) > 0:
                block.append(rating)
            else:
                blocks.append(block)
                block = [rating]

    blocks.append(block)
    return blocks


def get_minimal_increasing_block(blocks):
    result = []
    for block in blocks:
        if block[0] < block[-1]:
            result.append([i+1 for i in range(len(block))])
        elif block[0] > block[-1]:
            result.append([len(block) - i for i in range(len(block))])
        else:
            result.append([1])
    return result

# ex: 1,2,3,4,2,1, -> [1,2,3,4], [2,1]

#print(Solution().candy([1, 0, 2]))
#print(Solution().candy([5,3,7,3]))
# print(Solution().candy([1, 2, 2]))
# print(Solution().candy([1, 3, 2, 2, 1]))
#print(Solution().candy([1, 3, 4, 5, 2]))
#print(Solution().candy([6,5,4,3,2,3,4,5 ]))
#print(Solution().candy([1,2,3,5,4,3,2,1]))
print(Solution().candy(
[1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]))
# [1, 2, 1, 2, 1]