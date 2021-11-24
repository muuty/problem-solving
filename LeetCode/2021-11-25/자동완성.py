def get_min_typing_count(word, word1):
    for i in range(len(word)):
        if len(word1) > i:
            if word[i] == word1[i]:
                continue
        return i + 1
    return len(word)

def solution(words):
    words.sort()
    count = 0
    for i in range(len(words)):
        if i == 0:
            min_type = get_min_typing_count(words[i], words[i+1])
        elif i == len(words)-1:
            min_type = get_min_typing_count(words[i], words[i-1])
        else:
            min_type = max([get_min_typing_count(words[i], words[i+1]), get_min_typing_count(words[i], words[i-1])])
        count += min_type
    return count


#print(get_min_typing_count("go", "gone"))
print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]	))
print(solution(["aaaaa", "aaaab", "aaabb", "aabbb", "abbbb"]))
