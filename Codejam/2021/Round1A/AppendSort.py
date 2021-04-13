T = int(input())


for t in range(1, T+1):
    count = int(input())
    nums = list(input().split())
    answer = 0
    for i in range(len(nums)):
        if i==0:
            continue

        if len(nums[i]) > len(nums[i-1]):
            continue
        elif len(nums[i]) == len(nums[i-1]):
            if int(nums[i]) <= int(nums[i-1]):
                nums[i] += '0'
                answer += 1
                continue
            else:
                continue
        elif len(nums[i]) < len(nums[i-1]):
            my_len = len(nums[i])
            len_diff = (len(nums[i - 1]) - len(nums[i]))
            if nums[i][0:my_len] > nums[i-1][0:my_len]:
                len_diff = (len(nums[i-1]) - len(nums[i]))
                nums[i] += '0' * len_diff
                answer += len_diff
            elif nums[i][0:my_len] == nums[i-1][0:my_len]:
                if nums[i-1][my_len:] == '9' * len_diff:
                    nums[i] += '0' * (len_diff +1)
                    answer += len_diff + 1
                else:
                    plus = str(int(nums[i-1][my_len:]) + 1)
                    if len(plus) != len_diff:
                        plus = '0' *(len_diff - len(plus)) + plus
                    nums[i] += plus
                    answer += len_diff
            else:
                nums[i] += '0' * (len_diff + 1)
                answer += len_diff + 1

    print("Case #" + str(t) + ":" , answer)
