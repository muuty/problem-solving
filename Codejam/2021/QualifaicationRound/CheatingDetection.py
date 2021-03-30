import sys
import numpy as np

readline = sys.stdin.readline

T = int(input())
P = int(input())

for t in range(1, T + 1):
    score_list = []
    for i in range(0, 100):
        score_list.append(list(int(char) for char in readline()[:-1]))
    score_list = np.array(score_list)

    probs = np.sum(score_list, axis=0)
    sorted_array = probs.argsort()
    easy_index = sorted_array[:500]
    diff_index = sorted_array[-500:]
    mid_index = sorted_array[4750:5250]

    easy_probs = score_list[:, easy_index]
    diff_probs = score_list[:, diff_index]
    mid_probs = score_list[:, mid_index]



    score_in_easy_probs = np.sum(easy_probs, axis=1)
    score_in_diff_probs = np.sum(diff_probs, axis=1)
    score_in_mid_probs = np.sum(mid_probs, axis=1)

    diffs = [np.std([score_in_diff_probs[i],score_in_easy_probs[i],score_in_mid_probs[i]]) for i in range(0, 100)]
    print("Case #" + str(t) + ": ", diffs.index(min(diffs)) + 1)