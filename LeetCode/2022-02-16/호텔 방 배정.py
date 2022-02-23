def check_in_room(answer, room, next_empty_room):
    answer.append(room)
    next_empty_room[room] = room + 1


def solution(k, room_number):
    next_empty_room = {}
    answer = []
    for room in room_number:
        if room not in next_empty_room:
            check_in_room(answer, room, next_empty_room)

        else:
            pending = []
            searched_room = room
            while True:
                searched_room = next_empty_room[searched_room]
                if searched_room not in next_empty_room:
                    check_in_room(answer, searched_room, next_empty_room)
                    break
                else:
                    pending.append(searched_room)
            for _room in pending:
                next_empty_room[_room] = searched_room + 1
    return answer

print(solution(10, [1,3,4,1,3,1]))