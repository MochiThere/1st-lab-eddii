from queue import Queue
from typing import Any, Optional, Tuple

class Node:
    def __init__(self, data: Optional[Any] = None) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root
    
    #RECORRIDOS R-NR
    def preorden_r(self, node: Node) -> None:
        if (node is not None):
            print(node.data, end = " ")
            self.preorden_r(node.left)
            self.preorden_r(node.right)
     
    def preorden_nr(self, root: Node) -> None:
        stack: list[Node] = []
        pointer = root
        while (pointer is not None or len(stack) > 0):
            if (pointer is not None):
                print(pointer.data, end = " ")
                stack.append(pointer)
                pointer = pointer.left
            else:
                pointer = stack.pop()
                pointer = pointer.right
                
    def inorden_r(self, node: Node) -> None:
        if (node is not None):
            self.inorden_r(node.left)
            print(node.data, end = " ")
            self.inorden_r(node.right)
            
    
    def inorden_nr(self, root: Node) -> None:
        stack: list[Node] = []
        pointer = root
        while (pointer is not None or len(stack) > 0):
            if pointer is not None:
                stack.append(pointer)
                pointer = pointer.left
            else:
                pointer = stack.pop()
                print(pointer.data, end = " ")
                pointer = pointer.right
                
    def posorden_r(self, node: Node) -> None:
        if node is not None:
            self.posorden_r(node.left)
            self.posorden_r(node.right)
            print(node.data, end = " ")
         
    def posorden_nr(self, root: Node) -> None:
        stack: list[Node] = []
        out: list[Node] = []
        stack.append(root)
        
        while (len(stack) > 0):
            pointer = stack.pop()
            out.append(pointer)
            if pointer.left is not None:
                stack.append(pointer.left)
            if pointer.right is not None:
                stack.append(pointer.right)
                
        while len(out) > 0:
            print(out.pop().data, end = " ")                       
    
    def por_niveles_nr(self, root: Optional[Node]) -> None:
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
            
    #ATRIBUTOS DEL ARBOL
    def altura_de_un_arbol_r (self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return (1 + max(self.altura_de_un_arbol_r(node.left), self.altura_de_un_arbol_r(node.right)))
        
    #ARBOL BINARIO GENÉRICO
    @staticmethod
    def generate_sample_binary_tree() -> "BinaryTree":
        T = BinaryTree(Node('A'))
        T.root.left = Node('B')
        T.root.right = Node('C')
        T.root.left.left = Node('D')
        T.root.left.right = Node('E')
        T.root.right.right = Node('F')
        T.root.left.left.left = Node('G')
        T.root.left.left.right = Node('H')
        T.root.right.right.left = Node('I')
        T.root.right.right.right = Node('J')
        T.root.left.left.right.left = Node('K')

        return T
    

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
                    

print("-----CREAMOS EL ABB VACIO-----")
bst = BinarySearchTree()
print(bst.root)
print()

print("-----INSERTAMOS RAIZ-----")
print(BinarySearchTree.insert(bst, 62))
print()

print("-----INSERTAMOS HIJOS-----")
print(BinarySearchTree.insert(bst, 49))
print(BinarySearchTree.insert(bst, 78))
print(BinarySearchTree.insert(bst, 31))
print(BinarySearchTree.insert(bst, 55))
print(BinarySearchTree.insert(bst, 69))
print(BinarySearchTree.insert(bst, 90))
print(BinarySearchTree.insert(bst, 10))
print(BinarySearchTree.insert(bst, 37))
print(BinarySearchTree.insert(bst, 66))
print(BinarySearchTree.insert(bst, 96))
print(BinarySearchTree.insert(bst, 93))
print()

print("-----RECORRIDOS-----")
print("Preorden")
bst.preorden_nr(bst.root)
print()
print("Inorden")
bst.inorden_nr(bst.root)
print()
print("Postorden")
bst.posorden_nr(bst.root)
print()

print("-----ELIMINAMOS ALGUNOS NODOS-----")
print(BinarySearchTree.delete(bst, 49))
print(BinarySearchTree.delete(bst, 37))
print(BinarySearchTree.delete(bst, 62))
print(BinarySearchTree.delete(bst, 90))
print(BinarySearchTree.delete(bst, 78))
print(BinarySearchTree.delete(bst, 15))

print("-----RECORRIDOS X2-----")
print("Preorden")
bst.preorden_nr(bst.root)
print()
print("Inorden")
bst.inorden_nr(bst.root)
print()
print("Postorden")
bst.posorden_nr(bst.root)
print()