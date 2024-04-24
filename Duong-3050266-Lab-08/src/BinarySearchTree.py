"""
Author: Stanley Hsu
KUID: 3131322
Date: 3/12/24
Lab: Lab_6
Last modified: 3/27/2024
Purpose: to create a functional binary search tree using nodes


"""
'''nodes'''
class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
'''tree class'''
class BinarySearchTree:
    def __init__(self):
        self._root_node = None
    '''recursively adds the node and is apart of the add function'''
    def _recursive_add(self, current_node, new_node):
        if current_node.value is None:
            current_node.value = new_node.value
        elif new_node.value < current_node.value:
            if current_node.left:
                self._recursive_add(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self._recursive_add(current_node.right, new_node)
            else:
                current_node.right = new_node
        elif new_node.value == current_node.value:
            raise ValueError(
                f"Duplicate value of: {new_node.value} was attempted to add to the BST, duplicate values are not allowed!"
            )
        else:
            raise RuntimeError(
                "An unknown exception occured while attempting to recursively add a node to the BST"
            )
    '''add function '''
    def add(self, value):
        root_node = self._root_node
        new_node = BinarySearchTreeNode(value)
        if root_node is None:
            self._root_node = new_node
        else:
            return self._recursive_add(root_node, new_node)

    '''returns the inorder traversal order'''
    def inorder(self, node=None, order=None):
        root_node = node or self._root_node
        order = order or []
        stack = []
        current = root_node
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                order.append(current.value)
                current = current.right
        return order
    '''returns the preorder traversal order'''
    def preorder(self, node=None, order=None):
        root_node = node or self._root_node
        order = order or []
        if root_node:
            order.append(root_node.value)

            if root_node.left:
                self.preorder(root_node.left, order)

            if root_node.right:
                self.preorder(root_node.right, order)

        return order
    '''returns the postorder traversal order'''
    def postorder(self, node=None, order=None):
        root_node = node or self._root_node
        order = order or []
        stack = []
        current = root_node
        visited = set()  # Set to track visited nodes

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and peek_node.right not in visited:
                    # Move to the right subtree if it exists and hasn't been visited yet
                    current = peek_node.right
                else:
                    # Process the node if its right subtree is None or has been visited
                    order.append(peek_node.value)
                    visited.add(peek_node)
                    stack.pop()

        return order

    def search(
        self,
        value,
        *keys,
        current_node = None,
    ):
        """
        This search function will return a whole node based on a subkey path.

        :value: any value to search for
        :key: property to access on node
        :example:
            pokedex.search(132, "id") # -> ditto

        """
        current_node = self._root_node if current_node is None else current_node

        if not current_node:
            return None

        current_value = current_node.value
        if current_value is None:
            return None

        for k in keys:
            # Of course this is unsafe
            current_value = getattr(current_value, k)  

        if value == current_value:
            return current_node
        elif value < current_value:
            return self.search(
                value,
                *keys,
                current_node=current_node.left if current_node.left else False,
            )
        elif value > current_value:
            return self.search(
                value,
                *keys,
                current_node=current_node.right if current_node.right else False,
            )

    def copy(self):
        values = self.preorder()
        copied_tree = BinarySearchTree()
        for value in values:
            copied_tree.add(value)
        return copied_tree

    def _min_value_node(
        self, node
    ):
        current = node
        while current.left is not None:
            current = current.left

        return current

    def remove(
        self,
        value,
        *keys,
        current_node = None,
    ):
        """
        Remove a node

        Returns a the new node after removal

        :value: any value to search for
        :key: property to access on node
        :example:
            pokedex.remove(12) # -> "Butterfree"
        """
        current_node = self._root_node if current_node is None else current_node

        if not current_node:
            return None

        current_value = current_node.value
        if current_value is None:
            return None

        for k in keys:
            # Of course this is unsafe
            current_value = getattr(current_value, k)  

        # print(value, current_value)

        if value < current_value:
            current_node.left = self.remove(value, *keys, current_node=current_node.left if current_node.left else False)  
        elif value > current_value:
            current_node.right = self.remove(value, *keys, current_node=current_node.right if current_node.right else False)  
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp

            temp = self._min_value_node(current_node.right)

            current_node.value = temp.value
            temp_value_compare = temp.value
            for k in keys:
                temp_value_compare = getattr(temp_value_compare, k)

            current_node.right = self.remove(temp_value_compare, *keys, current_node=current_node.right if current_node.right else False)  

        return current_node
