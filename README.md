# tree-coloring

## Assumptions
- Binary Tree, not Binary Search Tree
- STL functions in C++ would be much faster, using vectors
- Extra test file added `test5-modified.py`
- Note - didnt have enough time to create unittests, so left tests in separate files under tests folder

## Functional details
- findLeftPath - find left edges of the tree
- findRightPath - find right edges of the tree
- findLeafPath - find leaves (also edges)
- clean paths
    - Remove common nodes
    - Reverse right path
- Concatenate left, leaves and right paths
- printPreorderData - output node number in pre-order notation
- (loop)
    - addColors - find node 1 by 1 and change color based on path assignment
- printPreorderColors - output node color in pre-order notation

## Code analysis
### Time complexity
- findLeftPath-> O(log(n))
- findRightPath -> O(log(n))
- findLeafPath -> O(n)
- Clean paths and reverse -> O(n) 
- Concat ->  O(n)
- printPreorderData -> O(n)
- Loop - coloring -> O(n^2)
- printPreorderColors -> O(n)

### Worst case time complexity
- O(n^2)
- Can be improved to O(n) by replacing loop coloring function
- Can be improved to O(log(n)) by
    - creating leftList, leafList and rightList while adding nodes (in the beginning)

### Space complexity
- O(n) for nodes
- O(n) for paths
- O(n) for temporary storage/ vars