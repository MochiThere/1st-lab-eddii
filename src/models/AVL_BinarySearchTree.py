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
        pointer: Node = node
        aux: Node = None
        while (parent is not None):
            pointer = parent
            parent = self.search(pointer.data)[1]
            pointer.balance = self.calculate_balance(pointer)
            parent = self.search(pointer.data)[1]
            if pointer.balance == 2 or pointer.balance == -2:
                if pointer.balance == 2 and self.calculate_balance(pointer.right) == 1:
                    aux = self.simple_left_rotation(pointer)
                elif pointer.balance == -2 and self.calculate_balance(pointer.left) == -1:
                    aux = self.simple_right_rotation(pointer)
                elif pointer.balance == 2 and self.calculate_balance(pointer.right) == -1:
                    aux = self.double_right_left_rotation(pointer)
                elif pointer.balance == -2 and self.calculate_balance(pointer.left) == 1:
                    aux = self.double_left_right_rotation(pointer)
                else:
                    aux = self.simple_left_rotation(pointer)
                if parent is None:
                    self.root = aux
                elif(parent.right == pointer):
                    parent.right = aux
                else:
                    parent.left = aux
            
    
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
elements = [5,8,16,19,28,33,36,45,51,57,59,65,68,75,85,100]
for i in elements:
    print("-----insert " + str(i) + "-----")
    print(sample_tree.insert(i))
    sample_tree.by_levels()
    print()