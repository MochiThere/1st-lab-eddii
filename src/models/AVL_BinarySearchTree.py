from typing import Any, Optional, Tuple
from BinarySearchTree import BinarySearchTree
from Node import Node

class AVL_BinarySearchTree (BinarySearchTree):
    
    def __init__(self, root: Optional[Node]= None) -> None:
        super().__init__(root)
        
    def insert(self, element: Any) -> bool:
        return super().insert(element)
    
    def delete(self, element: Any) -> bool:
        return super().delete(element)
    
        
    def rebalance() -> bool:
        pass
    
    def ascendence (self, node: Node) -> None:
        pointer: Node = node
        parent: Optional[Node] = super().search(node.data)[1]
        while (parent is not None):
            parent.balance = self.calculate_balance(parent)
            pointer = parent
            parent = super().search(parent.data)[1]
    
    def calculate_balance (self, node: Node) -> int:
        return super().height(node.right) - super().height(node.left)
    
    def simple_left_rotation (self, node: Node) -> Node:
        pass
    
    def simple_right_rotation (self, node: Node) -> Node:
        pass
    
    def double_left_right_rotation (self, node: Node) -> Node:
        pass
    
    def double_right_left_rotation (self, node: Node) -> Node:
        pass
    
    
    
    