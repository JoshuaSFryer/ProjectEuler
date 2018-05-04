"""
Triangle containment
Problem 102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.

"""


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.slope = getSlope(p1, p2)
        self.intercept = getIntercept(p1, self.slope)

    def __str__(self):
        return "y = " + str(self.slope) + "x + " + str(self.intercept)

    def __repr__(self):
        return self.__str__()


def getSlope(p1: Point, p2: Point):
    if p2.x == p1.x:  # avoid division by zero
        return 10 ** 10  # Return an approximation of a straight vertical line
        # return "vertical"
    return (p2.y - p1.y)/(p2.x - p1.x)


def getIntercept(p: Point, slope: float):
    # Give this a sample point and a calculated slope
    # y = mx + b --> b = y - mx
    return p.y - slope * p.x


def solveEqn(x: float, l: Line):
    return l.slope * x + l.intercept


def midpoint(p1: Point, p2: Point):
    return Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)


def getOrientation(A: Point, B: Point, C: Point):
    """
    Determine whether point C lies above or below the line formed between AB
    """
    AB = Line(A, B)
    return C.y > solveEqn((A.x + B.x)/2, AB)





with open("problem_102_data.txt") as f:
    triangles = f.readlines()


inputPoints = triangles[0].replace("\n", "").split(",")


pointList = list()
for i in range(0, 5, 2):
    pointList.append(Point(int(inputPoints[i]), int(inputPoints[i+1])))


A = pointList[0]
B = pointList[1]
C = pointList[2]
origin = Point(0, 0)
print(A, B, C)

P = Point(3, 7)
Q = Point(3, 9)
L = Line(P, Q)
print(L)
print(solveEqn(4, L))
# print(checkContains(A, B, C, origin))




