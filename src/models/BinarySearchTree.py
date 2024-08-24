from typing import Any, Optional, Tuple
from Node import Node
from BinaryTree import BinaryTree

class BinarySearchTree (BinaryTree):
    def __init__ (self, root: Optional[Node] = None) -> None:
        super().__init__(root)
        
    def search(self, element: Optional[Any]) -> Tuple[Optional[Node], Optional[Node]]:
        pointer, parent = self.root, None
        while (pointer is not None):
            if (element == pointer.data):
                return pointer, parent
            else:
                parent = pointer
                if (element < pointer.data):
                    pointer = pointer.left
                else:
                    pointer = pointer.right
        return pointer, parent
    
    def insert(self, element: Any) -> bool:
        to_insert = Node(element)
        if self.root is None:
            self.root = to_insert
            return True
        else:
            pointer, parent = self.search(element)
            if pointer is not None:
                return False
            else:
                if element < parent.data:
                    parent.left = to_insert
                else:
                    parent.right = to_insert
            return True
    
    def delete (self, element: Any) -> bool:
        #Buscamos si existe el nodo a eliminar
        pointer: Optional[Node] = self.search(element)[0]
        parent: Optional[Node] = self.search(element)[1]
        if pointer is not None:
            #Caso 1: El nodo a eliminar no tiene hijos
            if (pointer.left is None and pointer.right is None):
                if (parent.left == pointer):
                    parent.left = None
                else:
                    parent.right = None
                del pointer
            #Caso 2.1: El nodo a eliminar tiene un hijo a la izq y no a la der
            elif (pointer.left is not None and pointer.right is None):
                if parent.left == pointer:
                    parent.left = pointer.left
                else:
                    parent.right = pointer.left
                del pointer
            #Caso 2.2: El nodo a eliminar no tiene un hijo a la izq pero si a la der
            elif (pointer.left is None and pointer.right is not None):
                if parent.left == pointer:
                    parent.left = pointer.right
                else:
                    parent.right = pointer.right
                del pointer
            #Caso 3: El nodo a eliminar tiene 2 hijos
            else:
                if (int(input("(1) predecesor, (#) sucesor: ")) == 1):
                    #Predecesor
                    pred: Node = self.predecesor(pointer)[0]
                    pred_parent: Node = self.predecesor(pointer)[1]
                    pred_son: Optional[Node] = self.predecesor(pointer)[2]
                    pointer.data = pred.data
                    if pointer == pred_parent:
                        pred_parent.left = pred_son
                    else:
                        pred_parent.right = pred_son
                    del pred
                else:
                    #Sucesor
                    sus: Node = self.sucesor(pointer)[0]
                    sus_parent: Node = self.sucesor(pointer)[1]
                    sus_son: Optional[Node] = self.sucesor(pointer)[2]
                    pointer.data = sus.data
                    if pointer == sus_parent:
                        sus_parent.right = sus_son
                    else:
                        sus_parent.left = sus_son
                    del sus
            return True
        return False         
            
    def predecesor(self, node: Node) -> list[Node, Node, Node]:
        pred: Node = node.left
        pred_parent: Node = node
        while (pred.right is not None):
            pred, pred_parent = pred.right, pred
        return pred, pred_parent, pred.left
            
    def sucesor(self, node: Node) -> list[Node, Node, Node]:
        sus: Node = node.right
        sus_parent: Node = node
        while (sus.left is not None):
            sus, sus_parent = sus.left, sus
        return sus, sus_parent, sus.right
