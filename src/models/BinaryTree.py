from queue import Queue
from typing import Any, Optional, Tuple
from .Node import Node

class BinaryTree:
    
    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root
    
    def preorder(self, node: Node) -> None:
        if (node is not None):
            print(node.data, end = " ")
            self.preorden_r(node.left)
            self.preorden_r(node.right)
            
    def inorder(self, node: Node) -> None:
        if (node is not None):
            self.inorden_r(node.left)
            print(node.data, end = " ")
            self.inorden_r(node.right)
                
    def posorder(self, node: Node) -> None:
        if node is not None:
            self.posorden_r(node.left)
            self.posorden_r(node.right)
            print(node.data, end = " ")
            
    def by_levels(self, root: Optional[Node]) -> None:
        queue = Queue()
        pointer = root
        queue.put(pointer)
        while(queue.not_empty):
            pointer = queue.get()
            print(pointer.data, end = " ")
            if pointer.left is not None:
                queue.put(pointer.left)
            if pointer.right is not None:
                queue.put(pointer.right)
            
    def height (self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return (1 + max(self.altura_de_un_arbol_r(node.left), self.altura_de_un_arbol_r(node.right)))