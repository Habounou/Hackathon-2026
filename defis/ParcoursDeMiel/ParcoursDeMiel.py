import math

points = []
dist = []
n = 0

def read_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(float, line.split(","))
            points.append((x, y))
    return points

def distance_matrix(points):
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        x1, y1 = points[i]
        for j in range(n):
            x2, y2 = points[j]
            matrix[i][j] = math.hypot(x2 - x1, y2 - y1)

    return matrix

def initialize(filename):
    global dist
    global n
    global points
    points = read_points(filename)
    #print(points)
    n = len(points)
    dist = distance_matrix(points)
    #print(dist)

def calculate_length(parcours):
    if parcours == None :
        return -1
    total_distance = 0
    num_points = len(parcours)
    
    for i in range(num_points):
        u = parcours[i]
        v = parcours[(i + 1) % num_points]
        total_distance += dist[u][v]
        
    return total_distance


def advise_honeybee():

    # *** recommandation : écrire votre code ici ***

    return None

if __name__ == "__main__":
    initialize("input_demo.txt")
    parcours_exemple = [i for i in range(n)]
    length = calculate_length(parcours_exemple)
    print(parcours_exemple)
    print(length)

    # pour le input_demo.txt, le meilleur parcours est [1, 0, 6, 5, 3, 2, 4]
    # 27.699768073747965
    #parcours_exemple = [1, 0, 6, 5, 3, 2, 4]

    best_answer = advise_honeybee()
    print(best_answer)
    print(calculate_length(best_answer))


