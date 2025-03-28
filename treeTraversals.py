


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


## building the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)


def inorder(tree):

    ## another base case
    if tree == None:
        return []

    ## base case
    if not tree.left and not tree.right:
        return [tree.value]

    return inorder(tree.left) + [tree.value] + inorder(tree.right)

print(inorder(root))


def preorder(tree):
    if not isinstance(tree, Node):
        return []

    print(f"Visiting Node with value: {tree.value}")  # Debugging output
    
    preorder_array = [tree.value] + preorder(tree.left) + preorder(tree.right)

    return preorder_array

preorder(root)

def postorder(tree):
    #base case
    if tree == None:
        return []
    
    return postorder(tree.left) + postorder(tree.right) + [tree.value]

print(postorder(root))

def levelOrderTreversal(tree):


    queuevalues = []
    queue = []
    res = []
    queue.append(tree)
    queuevalues.append(tree.value)
    while len(queue) > 0:

        curr_node = queue.pop()
        queuevalues.pop()
        res.append(curr_node.value)
        if curr_node.left:
            queuevalues.insert(0, curr_node.left.value)
            queue.insert(0, curr_node.left)
        if curr_node.right:
            queuevalues.insert(0, curr_node.right.value)
            queue.insert(0, curr_node.right)

        print("queue:", queuevalues)
        print("result:", res)
    

    return res

root1 = Node(5)
root1.left = Node(12)
root1.right = Node(13)
root1.left.left = Node(7)
root1.left.left.left = Node(17)
root1.left.left.right = Node(23)
root1.right = Node(13)
root1.right.right = Node(2)
root1.right.right.right = Node(11)
root1.right.right.left = Node(8)
root1.right.left = Node(14)
root1.right.left.left = Node(27)
root1.right.left.right = Node(3)

levelOrderTreversal(root1)