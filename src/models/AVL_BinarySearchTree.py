from typing import Any, Optional
from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree
from Node import Node

class AVL_BinarySearchTree (BinarySearchTree):
    
    def __init__(self, root: Optional[Node]= None) -> None:
        super().__init__(root)
        
    def insert(self, element: Any) -> bool:
        state: bool = super().insert(element)
        if state is True:
            self.rebalance(self.search(element)[0]) 
        return state
    
    def delete(self, element: Any) -> bool:
        state: bool =  super().delete(element)
        if state is True: 
            self.rebalance(self.search(element)[0])
        return state
    
    def rebalance (self, node: Node) -> None:
        parent: Optional[Node] = super().search(node.data)[1]
        while (parent is not None):
            parent.balance = self.calculate_balance(parent)
            print("parent: ")
            print(parent.data)
            print(parent.balance)
            if parent.balance == 2 or parent.balance == -2:
                if parent.balance == 2 and parent.right.balance == 1:
                    self.simple_left_rotation(parent)
                elif parent.balance == -2 and parent.left.balance == -1:
                    self.simple_right_rotation(parent)
                elif parent.balance == 2 and parent.right.balance == -1:
                    self.double_right_left_rotation(parent)
                elif parent.balance == -2 and parent.left.balance == 1:
                    self.double_left_right_rotation(parent)
                else:
                    self.simple_left_rotation(parent)
            parent = self.search(parent.data)[1]
    
    def calculate_balance (self, node: Node) -> int:
        return super().height(node.right) - super().height(node.left)
    
    def simple_left_rotation (self, node: Node) -> Node:
        print("slr")
        aux: Node = node.right
        node.right = aux.left
        aux.left = node
        return aux
    
    def simple_right_rotation (self, node: Node) -> Node:
        print("srr")
        aux: Node = node.left
        node.left = aux.right
        aux.right = node
        return aux
    
    def double_left_right_rotation (self, node: Node) -> Node:
        print("dlrr")
        node.left = self.simple_left_rotation(node.left)
        return self.simple_right_rotation(node)
    
    def double_right_left_rotation (self, node: Node) -> Node:
        print("drlr")
        node.right = self.simple_right_rotation(node.right)
        return self.simple_left_rotation(node)

print("-----Sample tree vacio-----")
sample_tree = AVL_BinarySearchTree()
print(sample_tree.root)
print("-----Insertar 5-----")
print(sample_tree.insert(5))
sample_tree.postorder(sample_tree.root)
print()
print("-----Insertar 15-----")
print(sample_tree.insert(15))
sample_tree.postorder(sample_tree.root)
print()
print("-----Insertar 10-----")
print(sample_tree.insert(10))
sample_tree.postorder(sample_tree.root)
print()
print("-----Insertar 7-----")
print(sample_tree.insert(7))
sample_tree.postorder(sample_tree.root)