# https://leetcode.com/problems/construct-quad-tree/description/


# We can construct a Quad-Tree from a two-dimensional area using the following steps:

#     If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
#     If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
#     Recurse for each of the children with the proper sub-grid.


# helper that checks same value


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


"""
take dimensions make Node
chekc for isSame
yes -> return node 
no -> fill out tl tr... for the node by recursing
return node
"""


def isSame(matrix, x1, y1, x2, y2):
    val = matrix[x1][y1]

    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            if matrix[row][col] != val:
                return False
    return True


# lol
def makeNode(matrix, x1, y1, x2, y2):
    if isSame(matrix, x1, y1, x2, y2):
        return Node(
            val=matrix[x1][y1],
            topLeft=None,
            bottomLeft=None,
            bottomRight=None,
            isLeaf=True,
            topRight=None,
        )
    else:
        return Node(
            matrix[x1][y1],
            False,
            makeNode(matrix, x1, y1, x2 // 2, y2 // 2),
            makeNode(matrix, x2 // 2, y2 // 2, x2, y2),
            makeNode(matrix, x1, y2 // 2, x2 // 2, y2 // 2),
            makeNode(matrix, x1, y1, x2, y2),
        )


def construct(self, grid):
    x1, y1, x2, y2 = 0, 0, len(grid) - 1, len(grid[0]) - 1

    return makeNode(grid, x1, y1, x2, y2)
