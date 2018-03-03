from tree_support import make_binary_tree_with_sorted_list,  BFS, pre_order_traversal, in_order_traversal, post_order_traversal, \
                        shortest_path_lenth_BST, Tree, tree_from_inorder_n_preorder


l = [i for i in range(0, 10)]


root = make_binary_tree_with_sorted_list(l)
root


inorder = in_order_traversal(root)
preorder = pre_order_traversal(root)
postorder = post_order_traversal(root)





def split(inorder, postorder):
    # postorder.reverse()
    for each in postorder:
        if each in inorder:
            break
    pivot = inorder.index(each)
    return inorder[pivot], inorder[:pivot], inorder[pivot + 1:]


def tree_from_inorder_n_postorder(inorder, postorder):
    while len(inorder) > 0 :
        pivot, left, right = split(inorder, postorder)
        tree = Tree(pivot, tree_from_inorder_n_postorder(left, postorder), tree_from_inorder_n_postorder(right, postorder))
        return tree
import copy
postorder = ['D', 'F', 'E', 'B', 'G', 'L', 'J', 'K', 'H', 'C', 'A']
inorder = ['D', 'B', 'F', 'E', 'A', 'G', 'C', 'L', 'J', 'H', 'K']


preorder = [10, 5, 1, 7, 40, 50]
p = preorder[:]
preorder.sort()
inorder = preorder
preorder = p
t = tree_from_inorder_n_preorder(inorder, preorder)
# test = copy.deepcopy(postorder)
# test.reverse()
# t1 = tree_from_inorder_n_postorder(inorder, test)
# path_lenth = shortest_path_lenth_BST(root, 1, 3)
# print(path_lenth)
# visited = BFS(root)


print('La')
