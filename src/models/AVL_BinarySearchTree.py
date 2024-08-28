from typing import Any, Optional
from BinarySearchTree import BinarySearchTree
from Movie import Movie
from Node import Node

class AVL_BinarySearchTree (BinarySearchTree):
    
    def __init__(self, root: Optional[Node]= None) -> None:
        super().__init__(root)
        
    def insert(self, element: Movie) -> bool:
        state: bool = super().insert(element)
        if state is True:
            self.rebalance(self.search(element.title)[0]) 
        return state
    
    def delete(self, element_key: str) -> bool:
        state: bool =  super().delete(element_key)
        if state is True: 
            self.rebalance(self.search(element_key)[1])
        return state
    
    def rebalance (self, node: Node) -> None:
        parent: Optional[Node] = super().search(node.key)[1]
        pointer: Node = node
        aux: Node = None
        while (parent is not None):
            pointer = parent
            parent = self.search(pointer.key)[1]
            pointer.balance = self.calculate_balance(pointer)
            parent = self.search(pointer.key)[1]
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
                    print("caso borde")
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
        aux: Node = node.right
        node.right = aux.left
        aux.left = node
        return aux
    
    def simple_right_rotation (self, node: Node) -> Node:
        aux: Node = node.left
        node.left = aux.right
        aux.right = node
        return aux
    
    def double_left_right_rotation (self, node: Node) -> Node:
        node.left = self.simple_left_rotation(node.left)
        return self.simple_right_rotation(node)
    
    def double_right_left_rotation (self, node: Node) -> Node:
        node.right = self.simple_right_rotation(node.right)
        return self.simple_left_rotation(node)

print("-----Sample tree vacio-----")
sample_tree = AVL_BinarySearchTree()
print(sample_tree.root)
elements = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
for i in elements:
    print("-----insert " + str(i) + "-----")
    print(sample_tree.insert(Movie(i,0,0,0,0,0,0)))
    sample_tree.inorder(sample_tree.root)
    print()

elements = ["a","d","e","g","h","j","l","n"]
for i in elements:
    print("-----delete " + str(i) + "-----")
    print(sample_tree.delete(i))
    sample_tree.inorder(sample_tree.root)
    print()