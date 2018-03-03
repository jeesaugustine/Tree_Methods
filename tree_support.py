import math


class Visited:
    def __init__(self):
        self.visited = []

    def make_visited(self, value):
        self.visited.append(value)

    def checked_visited(self, value):
        if value in self.visited:
            return True
        else:
            return False

    def get_full_visited(self):
        return self.visited


class Queue:
    def __init__(self, value=None):
        if value is None:
            self.values = []
        else:
            self.values = [value]

    def en_que(self, value):
        self.values.append(value)

    def de_queue(self):
        if len(self.values) > 0:
            val = self.values[0]
            del self.values[0]
            return val
        else:
            return None

    def len_queue(self):
        return len(self.values)


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def go_left(self):
        if self.left is not None:
            return self.left
        else:
            return None

    def go_right(self):
        if self.right is not None:
            return self.right
        else:
            return None

    def return_value(self):
        if self.value is None:
            return None
        else:
            return self.value


def make_binary_tree_with_sorted_list(lists):
    while len(lists) > 0:
        mid = math.floor(len(lists) / 2)
        list_left = lists[:mid]
        list_right = lists[mid + 1:]
        tree = Tree(lists[mid], make_binary_tree_with_sorted_list(list_left),
                    make_binary_tree_with_sorted_list(list_right))
        return tree


def BFS(root):
    q = Queue()
    v = Visited()
    if root:
        if root.left is not None:
            q.en_que(root.go_left())
        if root.right is not None:
            q.en_que(root.go_right())
        v.make_visited(root.return_value())
        # print(root.value)

    while q.len_queue() > 0:
        node = q.de_queue()
        v.make_visited(node.return_value())
        # print(node.value)
        if node.left is not None:
            q.en_que(node.go_left())
        if node.right is not None:
            q.en_que(node.go_right())

    return v.visited


def pre_order_traversal(node):
    v = Visited()
    pre_order_traversal_recursion(node, v)
    return v.get_full_visited()


def pre_order_traversal_recursion(node, v):
    v.make_visited(node.return_value())
    if node.return_value() is not None:
        if node.left is not None:
            pre_order_traversal_recursion(node.left, v)
        if node.right is not None:
            pre_order_traversal_recursion(node.right, v)


def post_order_traversal(node):
    v = Visited()
    post_order_traversal_recursion(node, v)
    return v.get_full_visited()


def post_order_traversal_recursion(node, v):
    if node.return_value() is not None:
        if node.left is not None:
            post_order_traversal_recursion(node.left, v)
        if node.right is not None:
            post_order_traversal_recursion(node.right, v)
        v.make_visited(node.return_value())


def in_order_traversal(node):
    v = Visited()
    in_order_traversal_recursion(node, v)
    return v.get_full_visited()


def in_order_traversal_recursion(node, v):
    """
    :param node: node for starting the exploration
    :param v: traversed list
    :return:
    """
    if node.return_value() is not None:
        if node.left is not None:
            in_order_traversal_recursion(node.left, v)
        v.make_visited(node.return_value())
        if node.right is not None:
            in_order_traversal_recursion(node.right, v)


def shortest_path_lenth_BST(node, key1, key2):
    """
    This method will return the correct values only if the Tree is BST
    This method also wishes the values in the tree to be unique
    :param node: Assumes the root of the tree as first
    :param key1: value 1 to be searched
    :param key2: value 1 to be searched
    :return:
    """
    if key1 == key2:
        return 0
    if node.return_value() is not None:
        if node.return_value() > key1 and node.return_value() > key2:
            return shortest_path_lenth_BST(node.go_left(), key1, key2)
        elif node.return_value() < key1 and node.return_value() < key2:
            return shortest_path_lenth_BST(node.go_right(), key1, key2)
        elif (key1 <= node.return_value() <= key2) or (key1 >= node.return_value() >= key2):
            if key1 > key2:
                tmp = key1
                key1 = key2
                key2 = tmp
            left_ptr = node
            left_counter = 0
            right_ptr = node
            right_counter = 0
            left_found = False
            right_found = False
            if left_ptr.return_value() == key1:
                left_found = True
            if right_ptr.return_value() == key2:
                right_found = True
            while left_ptr.return_value() is not None:
                if left_ptr.return_value() < key1:
                    left_ptr = left_ptr.go_right()
                elif left_ptr.return_value() > key1:
                    left_ptr = left_ptr.go_left()
                left_counter += 1
                if left_ptr is not None:
                    if left_ptr.return_value() == key1:
                        left_found = True
                        break
                else:
                    break
            while right_ptr.return_value() is not None:
                if right_ptr.return_value() < key2:
                    right_ptr = right_ptr.go_right()
                elif right_ptr.return_value() > key1:
                    right_ptr = right_ptr.go_left()
                right_counter += 1
                if right_ptr is not None:
                    if right_ptr.return_value() == key2:
                        right_found = True
                        break
                else:
                    break

            if left_found and right_found:
                return left_counter + right_counter
            else:
                if not left_found:
                    print('Key ', key1, 'not found in tree')
                elif not right_found:
                    print('Key ', key2, 'not found in tree')
                return 0


def splits(inorder, preorder):
    for each in preorder:
        if each in inorder:
            break
    pivot = inorder.index(each)
    return inorder[pivot], inorder[:pivot], inorder[pivot+1:]


def tree_from_inorder_n_preorder(inorder, preorder):
    while len(inorder) > 0:
        pivot, left, right = splits(inorder, preorder)
        tree = Tree(pivot, tree_from_inorder_n_preorder(left, preorder), tree_from_inorder_n_preorder(right, preorder))
        return tree