from copy import deepcopy


def get_min_move(char1, char2):
    value = abs(ord(char1) - ord(char2))
    n = 26
    return min([value, n - value])


def is_same(name1, name2):
    for i in range(len(name1)):
        if name1[i] != name2[i]:
            return False
    return True


def move(current_name, name, index, count, direction):
    current_name = deepcopy(current_name)

    changed = False
    if current_name[index] != name[index]:
        count += get_min_move(current_name[index], name[index])
        current_name[index] = name[index]
        changed = True

    print(current_name, index, count)

    if is_same(current_name, name):
        return count
    else:
        count += 1
        next_index = (index + direction + len(name)) % len(name)
        reverse_index = (index - direction + len(name)) % len(name)
        if changed:
            return min([move(current_name, name, next_index, count, direction),
                        move(current_name, name, reverse_index, count, -direction)])
        else:
            return move(current_name, name, next_index, count, direction)


def solution(name):
    n = len(name)
    current_name = ['A'] * n
    move_count = 0

    return move(current_name, name, 0, move_count, 1)


if __name__ == '__main__':
    print(solution("BBBAAAB"))