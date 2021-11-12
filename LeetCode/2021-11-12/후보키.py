def update_key(key, originals):
    updated = [original for original in originals if not key.issubset(set(original))]
    updated.append(key)
    return updated


def is_valid_keys(keys, relation):
    mapping = dict()
    for index, row in enumerate(relation):
        check_key = ','.join([row[key] for key in keys])
        if check_key in mapping:
            return False
        mapping[check_key] = True
    return True


def dfs(keys, i, relation, result):
    using_keys = set([key for key in keys if keys[key]])
    if is_valid_keys(using_keys, relation):
        result[0] = update_key(using_keys, result[0])
        return
    for key in range(i + 1, len(relation[0])):
        if not keys[key]:
            keys[key] = True
            dfs(keys, key, relation, result)
            keys[key] = False


def solution(relation):
    keys = {key: False for key in range(len(relation[0]))}
    result = [[]]
    for i in range(0, len(relation[0])):
        keys[i] = True
        dfs(keys, i, relation, result)
        keys[i] = False
    return len(result[0])

#print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
#print(solution([["a","1","4"],["2","1","5"],["a","2","4"]]))
print(solution([["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]]))