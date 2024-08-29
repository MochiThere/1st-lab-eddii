from .movie import Movie
from .node import Node

class AVLTree():

    def __init__(self, root:Node= None) -> None:
        self.root = root
    
    # Operaciones básicas ============================================
    
    def insert(self, element: Movie ) -> bool:
        to_insert = Node(element)
        if self.root is None:
            self.root =to_insert
            return True
        else:
            pointer, parent = self.search(to_insert.key)
            if pointer is not None:
                return False
            else:
                if element.title < parent.key:
                    parent.left = to_insert
                else:
                    parent.right = to_insert

                self.rebalance(self.search(element.title)[0]) 
                return True
    
    def delete (self, element_key: str) -> bool:
        #Buscamos si existe el nodo a eliminar
        pointer, parent = self.search(element_key)

        if pointer is not None:
            #Caso 1: El nodo a eliminar no tiene hijos
            if (pointer.left is None and pointer.right is None):
                if (parent.left == pointer):
                    parent.left = None
                else:
                    parent.right = None
                del pointer

            #Caso 2.1: El nodo a eliminar tiene un hijo a la izq
            elif (pointer.left is not None and pointer.right is None):
                if parent.left == pointer:
                    parent.left = pointer.left
                else:
                    parent.right = pointer.left
                del pointer

            #Caso 2.2: El nodo a eliminar tiene un hijo a la der
            elif (pointer.left is None and pointer.right is not None):
                if parent.left == pointer:
                    parent.left = pointer.right
                else:
                    parent.right = pointer.right
                del pointer

            #Caso 3: El nodo a eliminar tiene 2 hijos
            else:
                sus: Node = self.__sus(pointer)[0]
                sus_parent: Node = self.__sus(pointer)[1]
                sus_son: Node = self.__sus(pointer)[2]
                pointer.key = sus.key
                if pointer == sus_parent:
                    sus_parent.right = sus_son
                else:
                    sus_parent.left = sus_son
                del sus
                
            self.rebalance(self.search(element_key)[1])
            return True
        return False    
    
    def search(self, element_key:str ) -> tuple[Node, Node]:
        pointer, parent = self.root, None
        while (pointer is not None):
            if (element_key == pointer.key):
                return pointer, parent
            else:
                parent = pointer
                if (element_key < pointer.key):
                    pointer = pointer.left
                else:
                    pointer = pointer.right
        return pointer, parent
    
    # Obtener propiedades ============================================

    def height (self, node:Node ) -> int:
        if node is None:
            return 0
        return (1 + max(self.height(node.left), self.height(node.right)))

    def __pred(self, node) :
        pred: Node = node.left
        pred_parent: Node = node
        while (pred.right is not None):
            pred, pred_parent = pred.right, pred
        return pred, pred_parent, pred.left
            
    def __sus(self, node):
        sus: Node = node.right
        sus_parent: Node = node
        while (sus.left is not None):
            sus, sus_parent = sus.left, sus
        return sus, sus_parent, sus.right

    # Relacionadas al balanceo (AVL) =================================
    
    def rebalance (self, node: Node) -> None:
        parent: Node = self.search(node.key)[1]
        pointer: Node = node
        aux: Node = None

        while (parent is not None):
            pointer = parent
            parent = self.search(pointer.key)[1]
            pointer.balance = self.calculate_balance(pointer)
            # parent = self.search(pointer.key)[1]
            if abs(pointer.balance) == 2 :

                right_balance = self.calculate_balance(pointer.right)
                left_balance = self.calculate_balance(pointer.left)

                if pointer.balance == 2 and right_balance == 1:
                    aux = self.simple_left_rotation(pointer)

                elif pointer.balance == -2 and left_balance == -1:
                    aux = self.simple_right_rotation(pointer)

                elif pointer.balance == 2 and right_balance == -1:
                    aux = self.double_right_left_rotation(pointer)

                elif pointer.balance == -2 and left_balance == 1:
                    aux = self.double_left_right_rotation(pointer)

                else:
                    print("Borderline")
                    aux = self.simple_left_rotation(pointer)

                # Ayuda que es esto va dentro o fuera del if ?  
                if parent is None:
                    self.root = aux
                elif (parent.right == pointer):
                    parent.right = aux
                else:
                    parent.left = aux
            
    def calculate_balance (self, node: Node) -> int:
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)
    
    # Rotaciones ======================================================

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
    
    # Recorridos =======================================================

    def preorder(self, node:Node) -> None:
        if (node is not None):
            print(node.key, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node: Node) -> None:
        if (node is not None):
            self.inorder(node.left)
            print(node.key, end = " ")
            self.inorder(node.right)
                
    def postorder(self, node: Node) -> None:
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end = " ")
            
    def levels(self, node:Node, queue:list[Node]=[]) -> None:
        if node is not None:
            queue.append(node)
        
        if len(queue) > 0 :
            tmp = queue.pop(0)
            print(tmp.data)

            if tmp.left is not None:
                queue.append(tmp.left)

            if tmp.right is not None:
                queue.append(tmp.right)
            
            self.levels( None, queue )