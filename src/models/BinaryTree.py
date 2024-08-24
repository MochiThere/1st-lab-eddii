from queue import Queue
from typing import Any, Optional
from Node import Node

class BinaryTree:
    
    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root
    
    def preorder(self, node: Node) -> None:
        if (node is not None):
            print(node.data, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def inorder(self, node: Node) -> None:
        if (node is not None):
            self.inorder(node.left)
            print(node.data, end = " ")
            self.inorder(node.right)
                
    def postorder(self, node: Node) -> None:
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
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
        return (1 + max(self.height(node.left), self.height(node.right)))
    