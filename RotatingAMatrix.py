def rotate(matrix, direction):
    result = []
    for x in range(len(matrix)):
        result.append([])
    if direction == "clockwise":
        for x in range(len(matrix) - 1, -1, -1):
            for i in range(len(matrix[x])):
                result[i].append(matrix[x][i])
        return result
    elif direction == "counter-clockwise":
        for x in range(len(matrix) - 1, -1, -1):
            pos = 0
            for i in range(len(matrix[x]) - 1, -1, -1):
                result[pos].insert(0, matrix[x][i])
                pos +=1
        return result