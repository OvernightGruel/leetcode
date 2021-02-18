# array
# def traverse(array):
#     for i in range(len(array)):
#         print(array[i])
#
#
# traverse([1, 3, 4, 2, 5, 7])

# linked list
# class ListNode:
#
#     def __init__(self, val, next_node=None):
#         self.val = val
#         self.next = next_node
#
#
# def traverse(list_node):
#     if list_node is None:
#         return
#     # 前序遍历
#     print(list_node.val)
#     traverse(list_node.next)
#     # 后序遍历
#     # print(list_node.val)
#
#
# a = ListNode(6)
# b = ListNode(5, a)
# c = ListNode(4, b)
# d = ListNode(3, c)
# e = ListNode(2, d)
# f = ListNode(1, e)
#
# traverse(f)

# tree
# class TreeNode:
#
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def traverse(tree_node):
#     if tree_node is None:
#         return
#     # 前序遍历
#     print(tree_node.val)
#     traverse(tree_node.left)
#     # 中序遍历
#     # print(tree_node.val)
#     traverse(tree_node.right)
#     # 后序遍历
#     # print(tree_node.val)

class TreeNode:

    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def traverse(tree_node):
    if tree_node is None:
        return
    for children in tree_node.children:
        traverse(children)

