def solution(people, limit):

    people = sorted(people, reverse=True)
    left_index = 0
    right_index = len(people)-1
    count = 0
    while left_index < right_index:
        if people[left_index] + people[right_index] <= limit:
            left_index += 1
            right_index -= 1
            count += 1
        else:
            left_index += 1

    answer = count + (len(people) - 2*count)
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50]	, 100))
    print(solution([70, 80, 50]	, 100))
    #print(solution("4177252841", 8))
