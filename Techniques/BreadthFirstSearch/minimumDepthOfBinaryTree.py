'''
Minimum Depth of Binary Tree

* Use Level Order Traversal to find the leaf node 
* Return that value

'''



'''
Data structure for the element of the tree
'''
class Node(self,data):
    def __init__(self,data):
        self.value=data
        self.left =None
        self.right=None

def minDepth(root):
    if root is None:
        return 0
    
    q = []
    q.append({'node':root,'depth':1})
    
    while(len(q)>0):
        queueItem = q.pop(0);
        
        node = queueItem['node']
        depth = queueItem('depth')
        
        if node.left is None and node.right is None:
            return depth
        
        if node.left is not None:
            q.append({'node':node.left,'depth':depth+1})
        
        if node.right is not None:
            q.append({'node':node.right,'depth':depth+1})
        
        
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(minDepth(root))
    
    
main()