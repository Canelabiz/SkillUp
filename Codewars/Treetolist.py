# Codewars Tree to list
# https://www.codewars.com/kata/56ef9790740d30a7ff000199/train/python


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

    def __iter__(self):
        for x in range(self.n):
            yield x


def tree_to_list(tree_root):
    # print(f"{nodes.data= } - {nodes.child_nodes= }")
    return [node.data for node in tree_root]


print(tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])))
