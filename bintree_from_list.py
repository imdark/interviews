class Node():
    def count(self):
        curr_node = self
        length = 0
        while curr_node.next is not None:
            curr_node = curr_node.next
            length += 1
        return length

    def  find_offset(self, offset):
        curr_node = self
        length = 0
        if offset > 0:
            while length != offset and curr_node.next is not None:
                curr_node = curr_node.next
                length += 1
        else:
            while length != offset and curr_node.prev is not None:
                curr_node = curr_node.prev
                length -= 1
        return curr_node

    def __init__(self, prev, next, value: int):
        self.prev = prev
        self.next = next
        self.value = value

class DoublyLinkedList():
    def __init__(self, head : Node):
        self.head = head
    
    def from_list(lst):
        curr_node = Node(None, None, 0)
        double_list = DoublyLinkedList(curr_node)
        for val in lst:
            curr_node.value = val
            curr_node.next = Node(None, None, 0)
            curr_node.prev = curr_node
            curr_node = curr_node.next

        return double_list


    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
class Leaf:
    def __init__(self, left, right, value: int):
        self.left = left
        self.right = right
        self.value = value
    
    def from_node(node, curr_count):
        curr_node = node
        curr_leaf = Leaf(None, None, 0)
        curr_leaf.value = node.value

        if curr_count > 0:
            middle_index = curr_count // 2
            right_node = curr_node.find_offset(middle_index)
            curr_leaf.right = Leaf.from_node(right_node, middle_index)

            left_node = curr_node.find_offset(-middle_index)
            curr_leaf.left = Leaf.from_node(left_node, -middle_index)

        return curr_leaf

    def print(self):
        print(self.value)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()


class Tree:
    def __init__(self, root : Leaf):
        self.root = root
    
    def from_dbl_list(dbl_list : DoublyLinkedList):
        curr_node = dbl_list.head
        curr_count = curr_node.count() // 2
        middle_node = curr_node.find_offset(curr_count)
        root = Leaf.from_node(middle_node,  curr_count)

        tree = Tree(root)
        curr_leaf = root

        return tree

    def print(self):
        self.root.print()

def main():
    print('list: ')
    lst = DoublyLinkedList.from_list([1,2,3,4])
    lst.print()
    tree = Tree.from_dbl_list(lst)
    print('tree: ')
    tree.print()
    
if __name__ == '__main__':
    main()
    
# log(n) * n
