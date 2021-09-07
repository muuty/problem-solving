def str_to_sec(hhmm):
    hh, mm = hhmm.split(":")
    return int(hh) * 60 + int(mm)

def sec_to_str(sec):
    hh = str(sec//60)
    if len(hh) == 1:
        hh = "0" + hh
    ss = str(sec%60)
    if len(ss) == 1:
        ss = "0" + ss

    return hh + ":" + ss


def solution(n, t, m, timetable):
    start_time = str_to_sec("09:00")
    bus_table = [(start_time + i*t,"B") for i in range(n)]
    person_table = sorted([(str_to_sec(time),"A") for time in timetable])
    events = sorted(bus_table + person_table)

    current_waiting = 0
    current_bus = 0
    bus_people_sum = 0
    for event in events:
        time, event_type = event
        if event_type == "A":
            current_waiting += 1
        else:
            current_bus += 1
            bus_people = m if current_waiting >= m else current_waiting
            current_waiting -= bus_people
            bus_people_sum += bus_people
            if current_bus == n:
                if bus_people == m:
                    answer = sec_to_str(person_table[bus_people_sum - 1][0] - 1)
                    break
                else:
                    answer = sec_to_str(time)

    return answer


print(solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,1	,2,	["09:00", "09:00", "09:00", "09:00"]))