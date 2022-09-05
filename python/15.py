# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right
# corner.
#
# How many such routes are there through a 20×20 grid?
# https://projecteuler.net/problem=15

import string, sys
import commonutils

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.point == other.point

def buildGraph(node, terminal, allNodes):
    """
    Build a graph representing the points which are part of the grid and their
    adjacency.
    For example:
    (0,0)
        -> (0,1)
            -> (0,2)
            -> (1,1)
        -> (1,0)
            -> (1,1)
            -> (2,1)
    ...
    and so on
    """
    if node == terminal:
        return

    buildLeftTree(node, terminal, allNodes)
    buildRightTree(node, terminal, allNodes)

def buildLeftTree(node, terminal, allNodes):
    """
    Build the left tree of the current node
    """
    leftPoint = (node.point[0]+1, node.point[1])

    leftNode = None
    if str(leftPoint) in allNodes.keys():
        leftNode = allNodes[str(leftPoint)]
    else:
        leftNode = Node(leftPoint)
        allNodes[str(leftPoint)] = leftNode

    node.left = leftNode

    if leftPoint[0] != terminal.point[0]:
        buildGraph(leftNode, terminal, allNodes)

def buildRightTree(node, terminal, allNodes):
    """
    Build the right tree of the current node
    """
    rightPoint = (node.point[0], node.point[1]+1)

    rightNode = None
    if str(rightPoint) in allNodes.keys():
        rightNode = allNodes[str(rightPoint)]
    else:
        rightNode = Node(rightPoint)
        allNodes[str(rightPoint)] = rightNode

    node.right = rightNode

    if rightPoint[1] != terminal.point[1]:
        buildGraph(rightNode, terminal, allNodes)

def printGraph(node, level=0):
    tab = level * "\t"
    pointStr = str(node.point)
    print(f"{tab} {pointStr}")
    if node.left:
        printGraph(node.left, level+1)
    if node.right:
        printGraph(node.right, level+1)

def main():
    gridSize = 2
    startPoint = (0,0)
    endPoint = (gridSize, gridSize)

    root = Node(startPoint)
    terminal = Node(endPoint)

    allNodes = {}
    allNodes[str(root.point)] = root
    allNodes[str(terminal.point)] = terminal

    buildGraph(root, terminal, allNodes)
    printGraph(root)

if __name__ == '__main__':
    main()
