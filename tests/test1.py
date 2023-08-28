import numpy as np
import sys
sys.path.append('')
import tree.globals as globals

from tree.node import *

# Driver code
if __name__ == '__main__':
    # Root
    root = Node(1)

    # Function call
    globals.initialize()
    
    findLeftPath(root)
    findRightPath(root)
    findLeaves(root)

    # Clean up and create path
    if(len(globals.leafList) > 1):
        globals.leafList = np.delete(globals.leafList, 0) 
    if(len(globals.rightList) > 1):
        globals.rightList = np.delete(globals.rightList, -1) 
        globals.rightList = np.delete(globals.rightList, 0) 
        globals.rightList = globals.rightList[::-1]
    
    x = np.concatenate((globals.leftList, globals.leafList, globals.rightList))
    res,ind = np.unique(x, return_index=True)
    x = res[np.argsort(ind)]
    
    print(f"Counter-clockwise path: \n{x}\n")
    print("Preorder traversal:")
    printPreorderData(root)
    j = 0
    for i in x:
        addColors(root, i, j)
        j=j+1
    print(f"")
    printPreorderColors(root)