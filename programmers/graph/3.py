def point2str(p):
    return ','.join(map(str,p))

def edge2str(p1,p2):
    return ','.join(map(str,p1)) + "->" + ','.join(map(str, p2))

def get_next_points(p, v):
    return [p[0] + v[0], p[1] + v[1]], [p[0] + v[0] /2, p[1] + v[1]/2]

def solution(arrows):
    points = {"0,0" : True}
    edges = {}
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    previous_point = [0,0]
    for arrow in arrows:
        current_point, half_point = get_next_points(previous_point, directions[arrow])
        points[point2str(current_point)] = True
        points[point2str(half_point)] = True

        edges[edge2str(previous_point, half_point)] = True
        edges[edge2str(half_point, previous_point)] = True

        edges[edge2str(half_point, current_point)] = True
        edges[edge2str(current_point, half_point)] = True
        previous_point = current_point

    return 1 - len(points) + len(edges)//2



if __name__ == '__main__':
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	))
    print(solution([0,2,4,6, 0,2,4,6 ,0,2,4,6]))
    print(solution([1,3,5,7]	))
    print(solution([1,4,4,7,7,4,4,1,1]))
    print(solution([3,0,0,5,5,0,0,3,3]))
    print(solution([5,0,0,3,3,0,0,5,5]))
    print(solution([7,4,4,1,1,4,4,7,7]))

    print(solution([0,0,2,2,4,4,6,6,0,1,3,5,7]))
    print(solution([0,0,2,2,4,4,6,6,0,1,3,5,7,0,3,3,0,0,5,5]))
    print(solution([0, 0, 2, 2, 4, 4, 6, 6, 0, 1, 3, 5, 7, 0, 3, 3, 0, 0, 5, 5, 0,2,2]))
    print(solution([1,4,4,7,7,4,4,1,1]))

    print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]), 3)
    print(solution([5,2,7,1,6,3]),3)
    print(solution([6,2,4,0,5,0,6,4,2,4,2,0]), 3)

'''
def is_cross_exists(arrow, point, edges):
    if arrow == 1:
        point1 = [point[0] + 1, point[1] ]
        point2 = [point[0] , point[1] + 1 ]
        edge = ','.join(map(str,point1)) + "->" + ','.join(map(str, point2))
        if edge in edges:
            return True
    elif arrow == 3:
        point1 = [point[0] + 1, point[1] ]
        point2 = [point[0] , point[1] - 1]
        edge = ','.join(map(str,point1)) + "->" + ','.join(map(str, point2))
        if edge in edges:
            return True

    elif arrow == 5:
        point1 = [point[0] - 1, point[1]]
        point2 = [point[0], point[1] - 1]
        edge = ','.join(map(str,point1)) + "->" + ','.join(map(str, point2))
        if edge in edges:
            return True
    elif arrow == 7:
        point1 = [point[0] - 1, point[1]]
        point2 = [point[0], point[1] + 1]
        edge = ','.join(map(str,point1)) + "->" + ','.join(map(str, point2))
        if edge in edges:
            return True

    return False

def get_next_point(point, arrow):
    if arrow == 0:
        return [point[0] , point[1] + 1]
    elif arrow == 1:
        return [point[0] + 1 , point[1] + 1]
    elif arrow == 2:
        return [point[0] + 1, point[1]]
    elif arrow == 3:
        return [point[0] + 1, point[1] - 1]
    elif arrow == 4:
        return [point[0], point[1] - 1]
    elif arrow == 5:
        return [point[0] - 1, point[1] -1]
    elif arrow == 6:
        return [point[0] - 1, point[1] ]
    elif arrow == 7:
        return [point[0] - 1, point[1] + 1]


def solution(arrows):
    points = {"0,0" : True}
    edges = {}
    count = 0
    previous_point = [0,0]
    for arrow in arrows:
        current_point = get_next_point(previous_point, arrow)
        edge1 = ','.join(map(str,previous_point)) + "->" + ','.join(map(str, current_point))
        edge2 = ','.join(map(str,current_point)) + "->" + ','.join(map(str, previous_point))
        current_point_str = ','.join(map(str,current_point))
        if is_cross_exists(arrow, previous_point, edges):
            count += 1
        if current_point_str in points and edge1 not in edges and edge2 not in edges:
            count += 1
        points[current_point_str] = True
        edges[edge1] = True
        edges[edge2] = True

        previous_point = current_point
    return count'''