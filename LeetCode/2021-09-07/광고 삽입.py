
def hhmmss2s(hhmmss):
    if hhmmss == '0':
        return 0
    hh, mm, ss = hhmmss.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

def s2hhmmss(s):
    hh = str(s//3600)
    mm = str((s%3600)//60)
    ss = str(s%60)
    if len(hh) == 1:
        hh = "0" + hh
    if len(mm) == 1:
        mm = "0" + mm
    if len(ss) == 1:
        ss = "0" + ss
    return hh + ":" + mm + ":" + ss


    return str(s//3600) + str(m//60) + str(s%60)

def solution(play_time, adv_time, logs):
    play_time = hhmmss2s(play_time)
    adv_time = hhmmss2s(adv_time)
    times = [0] * (play_time + 1)
    for log in logs:
        start_time, end_time = [hhmmss2s(time) for time in log.split("-")]
        times[start_time] = 1
        times[end_time] = -1

    for i in range(1, len(times)):
        times[i] = times[i] + times[i - 1]


    cur_adv_time = 0
    for i in range(adv_time):
        cur_adv_time += times[i]

    max_adv_time = cur_adv_time
    max_start_time = 0
    for i in range(play_time - adv_time):
        if times[i + adv_time] == times[i]:
            continue
        cur_adv_time += times[i + adv_time] - times[i]
        if cur_adv_time > max_adv_time:
            max_adv_time = cur_adv_time
            max_start_time = i + 1

    return s2hhmmss(max_start_time)


print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	))