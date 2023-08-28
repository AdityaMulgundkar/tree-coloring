import numpy as np
import sys
sys.path.append('')
import tree.globals as globals
globals.initialize()

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None
        self.color = 'g'

def printPreorderData(node):
    if node is None:
        return
    print(node.data, end=' ')
    printPreorderData(node.left)
    printPreorderData(node.right)

def printPreorderColors(node):
    if node is None:
        return
    print(node.color, end=' ')
    printPreorderColors(node.left)
    printPreorderColors(node.right)
    
def findLeftPath(node):
    globals.leftList = np.append(globals.leftList, node.data)
    if(node.left == None and node.right == None):
        return
    if(node.left != None):
        findLeftPath(node.left)
    if(node.left == None):
        findLeftPath(node.right)

def findRightPath(node):
    globals.rightList = np.append(globals.rightList, node.data)
    if(node.left == None and node.right == None):
        return
    if(node.right != None):
        findRightPath(node.right)
    if(node.right == None):
        findRightPath(node.left)

def findLeaves(node):
    if(node.left == None and node.right == None):
        globals.leafList = np.append(globals.leafList, node.data)
    else:
        if(node.left != None):
            findLeaves(node.left)
        if(node.right != None):
            findLeaves(node.right)

def addColors(node, leaf, color):
    if(color%2==0):
        c = 'b'
    else:
        c = 'r'
    if(node == None):
        return
    if(node.data == leaf):
        if(color):
            node.color = c
        else:
            node.color = c
    addColors(node.left, leaf, color)
    addColors(node.right, leaf, color)
