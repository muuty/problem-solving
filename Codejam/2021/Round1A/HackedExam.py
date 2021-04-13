import operator as op
from functools import reduce
from fractions import Fraction
def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2


T = int(input())

def chageTF(char):
    if char == 'T':
        return 'F'
    else:
        return 'T'

for t in range(1, T+1):
    N, Q = map(int, input().split())
    answers = []
    scores = []
    final_answer = ['0'] * Q
    z=0
    w=1
    if N == 1:
        answer, score = input().split()
        score = int(score)

        if score >= len(answer) / 2.0:
            final_answer = answer
            z = score
            w = 1
        else:
            for i in range(Q):
                if answer[i] == 'T':
                    final_answer[i] = 'F'
                else:
                    final_answer[i] = 'T'
            z = len(answer) - score
            w = 1

    elif N == 2:
        for i in range(2):
            answer, score = input().split()
            score = int(score)
            answers.append(answer)
            scores.append(score)

        diff_part = [i for i in range(Q) if answers[0][i] != answers[1][i]]
        same_part = [i for i in range(Q) if answers[0][i] == answers[1][i]]
        l = len([i for i in range(Q) if answers[0][i] != answers[1][i]])
        s = (scores[0] + scores[1] - l)/2

        if s >=  len(same_part)/2:
            for i in range(Q):
                final_answer[i] = answers[0][i]
            z += s
        else:
            for i in range(Q):
                if answers[0][i] == 'T':
                    final_answer[i] = 'F'
                else:
                    final_answer[i] = 'T'

            z += len(same_part)-s
        if scores[0] >= scores[1]:
            for i in diff_part:
                final_answer[i] = answers[0][i]
            z += scores[0] - s
        else:
            for i in diff_part:
                final_answer[i] = answers[1][i]
            z += scores[1] - s

    elif N==3:
        for i in range(3):
            answer, score = input().split()
            score = int(score)
            answers.append(answer)
            scores.append(score)

        a0_part = [i for i in range(Q) if answers[0][i] == answers[1][i] and answers[1][i] == answers[2][i]]
        a1_part = [i for i in range(Q) if answers[0][i] != answers[1][i] and answers[1][i] == answers[2][i]]
        a2_part = [i for i in range(Q) if answers[1][i] != answers[0][i] and answers[0][i] == answers[2][i]]
        a3_part = [i for i in range(Q) if answers[2][i] != answers[0][i] and answers[0][i] == answers[1][i]]
        l0 = len(a0_part)
        l1 = len(a1_part)
        l2 = len(a2_part)
        l3 = len(a3_part)

        s1 = scores[0]
        s2 = scores[1]
        s3 = scores[2]

        a0_exp_score = 0
        a1_exp_score = 0
        a2_exp_score = 0
        a3_exp_score = 0
        not_a0_exp_score = 0
        not_a1_exp_score = 0
        not_a2_exp_score = 0
        not_a3_exp_score = 0

        total_count = 0
        for i in range(0, l0+1):
            a0 = i
            a1 = (2 * a0 + 2 * l1 + l2 + l3 - s2 - s3) // 2
            a2 = (2 * a0 + 2 * l2 + l1 + l3 - s1 - s3) // 2
            a3 = (2 * a0 + 2 * l3 + l1 + l2 - s1 - s2) // 2

            if l0 >= a0 >= 0 and l1 >= a1 >= 0 and l2 >= a2 >= 0 and l3 >= a3 >= 0:
                current_count = nCr(l0, a0) * nCr(l1, a1) * nCr(l2, a2) * nCr(l3, a3)
                total_count += current_count

                a0_exp_score += a0 * current_count
                not_a0_exp_score += (l0 - a0) * current_count
                a1_exp_score += a1 * current_count
                not_a1_exp_score += (l1 - a1) * current_count
                a2_exp_score += a2 * current_count
                not_a2_exp_score += (l2 - a2) * current_count
                a3_exp_score += a3 * current_count
                not_a3_exp_score += (l3 - a3 ) * current_count

        expected_scores = [0,0,0,0]

        for i in a0_part:
            if a0_exp_score >= not_a0_exp_score:
                final_answer[i] = answers[0][i]
                expected_scores[0] = (a0_exp_score, total_count)
            else:
                final_answer[i] = chageTF(answers[0][i])
                expected_scores[0] = (not_a0_exp_score, total_count)

        for i in a1_part:
            if a1_exp_score >=not_a1_exp_score:
                final_answer[i] = answers[0][i]
                expected_scores[1] = (a1_exp_score, total_count)
            else:
                final_answer[i] = chageTF(answers[0][i])
                expected_scores[1] = (not_a1_exp_score, total_count)

        for i in a2_part:
            if a2_exp_score >=not_a2_exp_score:
                final_answer[i] = answers[1][i]
                expected_scores[2] = (a2_exp_score, total_count)
            else:
                final_answer[i] = chageTF(answers[1][i])
                expected_scores[2] = (not_a2_exp_score, total_count)

        for i in a3_part:
            if a3_exp_score >=not_a3_exp_score:
                final_answer[i] = answers[2][i]
                expected_scores[3] = (a3_exp_score, total_count)
            else:
                final_answer[i] = chageTF(answers[2][i])
                expected_scores[3] = (not_a3_exp_score, total_count)


        z = sum([val[0] for val in expected_scores if val != 0])
        w = total_count
        fraction = Fraction(z,w)
        z = fraction.numerator
        w = fraction.denominator

    print("Case #" + str(t) + ": " + ''.join(final_answer) + " " + str(int(z)) + "/" + str(w))
