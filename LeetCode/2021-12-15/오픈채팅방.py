ENTER = 0
LEAVE = 1
CHANGE = 2
action_type = {"Enter": ENTER,
               "Leave": LEAVE,
               "Chang": CHANGE}

def get_action_type(record):
    return action_type[record[0:5]]

def solution(records):
    logs = []
    uid_to_name = {}
    answer = []
    for record in records:
        action_type = get_action_type(record)
        if action_type == ENTER:
            _, uid, name = record.split(' ')
            logs.append((uid, "님이 들어왔습니다."))
            uid_to_name[uid] = name
        elif action_type == LEAVE:
            _, uid = record.split(' ')
            logs.append((uid, "님이 나갔습니다."))
        elif action_type == CHANGE:
            _, uid, name = record.split(' ')
            uid_to_name[uid] = name

    for log in logs:
        answer.append(''.join([uid_to_name[log[0]],log[1]]))

    return answer


ENTER = 0
LEAVE = 1
CHANGE = 2
action_type = {"Enter": ENTER,
               "Leave": LEAVE,
               "Chang": CHANGE}
def get_action_type(record):
    return action_type[record[0:5]]

records1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records1))