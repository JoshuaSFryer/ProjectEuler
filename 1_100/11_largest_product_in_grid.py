"""
Largest product in a grid
Problem 11

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

[See problem_11_data.txt]

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

"""


with open("problem_11_data.txt", "r") as f:
    lines = f.readlines()

lineList = list()
for line in lines:
    # strip the newline characters
    line = line.replace("\n", "")
    lineList.append(line.split(" "))

# The numbers are now organized into a 2-dimensional array


def search(y, x, dir):
    # search in each of the diagonal and orthogonal directions and take the product of the selected element
    # and the next three in that direction.
    product = 1
    if dir == "n":
        if y - 3 >= 0:
            for i in range(y, y-4, -1):
                product *= int(lineList[i][x])

    elif dir == "s":
        if y + 3 <= 19:
            for i in range(y, y+4, 1):
                product *= int(lineList[i][x])

    elif dir == "w":
        if x - 3 >= 0:
            for i in range(x, x-4, -1):
                product *= int(lineList[y][i])

    elif dir == "e":
        if x + 3 <= 19:
            for i in range(x, x+4, 1):
                product *= int(lineList[y][i])

    elif dir == "nw":
        if y - 3 >= 0 and x - 3 >= 0:
            for i in range(0, 4):
                product *= int(lineList[y][x])
                x -= 1
                y -= 1

    elif dir == "ne":
        if y - 3 >= 0 and x + 3 <= 19:
            for i in range(0, 4):
                product *= int(lineList[y][x])
                x += 1
                y -= 1

    elif dir == "sw":
        if y + 3 <= 19 and x - 3 >= 0:
            for i in range(0,4):
                product *= int(lineList[y][x])
                x -= 1
                y += 1

    elif dir == "se":
        if y + 3 <= 19 and x + 3 <= 19:
            for i in range(0, 4):
                product *= int(lineList[y][x])
                x += 1
                y += 1

    return product


bestSoFar = 1
dirList = ["n", "s", "e", "w", "ne", "nw", "se", "sw"]
for i in range(0, 20):
    for j in range(0, 20):

        for direction in dirList:
            product = search(i, j, direction)
            if product > bestSoFar:
                bestSoFar = product


print(bestSoFar)