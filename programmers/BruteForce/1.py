def solution(answers):
    answer_1 = [1, 2, 3, 4, 5] * (10000 // 5 + 1)
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8 + 1)
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 8 + 1)
    answer_i = [answer_1, answer_2, answer_3]
    scores = [len([i for i in range(len(answers)) if answers[i] == answer_i[j][i]]) for j in range(3)]

    max_score = max(scores)
    max_index = [i + 1 for i in range(3) if scores[i] == max_score]

    return max_index