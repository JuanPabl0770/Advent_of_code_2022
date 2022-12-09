def check_for_visibility(rows, cols, posx, posy):

    # check if its edge tree
    if posx == 0 or posx == len(rows) - 1 or posy == 0 or posy == len(cols) - 1:
        return True

    # check row
    row = rows[posy]
    # check left visibility
    if max(row[:posx]) < row[posx]:
        return True
    # check right visibility
    if max(row[posx + 1:]) < row[posx]:
        return True
    # check col
    col = cols[posx]
    # check left visibility
    if max(col[:posy]) < col[posy]:
        return True
    # check right visibility
    if max(col[posy + 1:]) < col[posy]:
        return True

    return False


def get_scenic_score(rows, cols, posx, posy):

    # check if its edge tree
    if posx == 0 or posx == len(rows) - 1 or posy == 0 or posy == len(cols) - 1:
        return 0

    # check row
    row = rows[posy]
    # get left score
    l_score = 0
    for i in range(posx-1, -1, -1):
        if row[i] >= row[posx]:
            l_score += 1
            break
        l_score += 1

    # get right score
    r_score = 0
    for i in range(posx+1, len(row)):
        if row[i] >= row[posx]:
            r_score += 1
            break
        r_score += 1

    # check col
    col = cols[posx]
    # check up visibility
    u_score = 0
    for i in range(posy-1, -1, -1):
        if col[i] >= col[posy]:
            u_score += 1
            break
        u_score += 1

    # check down visibility
    d_score = 0
    for i in range(posy+1, len(col)):
        if col[i] >= col[posy]:
            d_score += 1
            break
        d_score += 1

    return l_score * r_score * u_score * d_score


f = open('input.txt', 'r')
lines = f.readlines()
size = len(lines)
cols = [[-1 for i in range(size)] for i in range(size)]
rows = [[-1 for i in range(size)] for i in range(size)]
for i, line in enumerate(lines):
    line = line.strip()
    for j, char in enumerate(line):
        rows[i][j] = char
        cols[j][i] = char

visible_trees = 0
for i in range(size):
    for j in range(size):
        if check_for_visibility(rows, cols, i, j):
            visible_trees += 1
print('number of visible trees: ',visible_trees)

highest_scenic_score = 0
for i in range(size):
    for j in range(size):
        curr_scenic_score = get_scenic_score(rows,cols,i,j)
        if curr_scenic_score > highest_scenic_score:
            highest_scenic_score = curr_scenic_score
print('highest scenic score: ', highest_scenic_score)


f.close()
