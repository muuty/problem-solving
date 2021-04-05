def solution(routes):
    routes.sort(key=lambda x: x[1])
    cameras = []
    for route in routes:
        if cameras and cameras[-1] >= route[0]:
            continue
        else:
            cameras.append(route[1])
    return len(cameras)