from classes.node import Node

tree = Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6)))


def traverse_tree(node):
    print(node.value)

    if node.right or node.left:
        if node.right:
            print(node.right.value)

            if node.right.right or node.right.left:
                traverse_tree(node.right.right if node.right.right else None)
                traverse_tree(node.right.left if node.right.left else None)

        if node.left:
            print(node.left.value)

            if node.left.right or node.left.left:
                traverse_tree(node.left.right if node.left.right else None)
                traverse_tree(node.left.left if node.left.left else None)


if __name__ == "__main__":
    traverse_tree(tree)
