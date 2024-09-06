from .movie import Movie
from .node import Node

class AVLTree():

    def __init__(self, root:Node= None) -> None:
        self.root = root
    
    # Operaciones básicas ============================================
    
    def insert(self, movie:Movie) -> bool:
        to_insert = Node(movie)

        # Inserción común
        if self.root is None:
            self.root = to_insert
            return True
        else:
            pointer, parent = self.search(to_insert.key)
            if pointer is not None:
                return False
            else:
                if to_insert.key < parent.key:
                    parent.left = to_insert
                else:
                    parent.right = to_insert
                self.rebalance(to_insert)
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
    
    def search(self, element_key:str ) -> tuple:
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
        # Calcular balances iniciales
        unbalances = self.calculate_ascendance(node)
        while (len(unbalances) > 0):
            # Seleccionar los desbalances en orden FIFO
            pointer = unbalances.pop(0)
            #padre del desbalance para reinsertar
            parent = self.search(pointer.key)[1]
            #calcular los balances de los hijos del desbalance
            if pointer.right is not None:
                pointer.right.balance = self.calculate_node_balance(pointer.right)
            if pointer.left is not None:
                pointer.left.balance = self.calculate_node_balance(pointer.left)
            #segun el tipo de desbalance hacer las rotaciones
            if pointer.balance == 2 and pointer.right.balance == 1:
                aux = self.simple_left_rotation(pointer)
            elif pointer.balance == -2 and pointer.left.balance == -1:
                aux = self.simple_right_rotation(pointer)
            elif pointer.balance == -2 and pointer.left.balance == 1:
                aux = self.double_left_right_rotation(pointer)
            elif pointer.balance == 2 and pointer.right.balance == -1:
                aux = self.double_right_left_rotation(pointer)
            else:
                aux = self.simple_left_rotation(pointer)
                
            #reasignar raiz / aux
            if (pointer == self.root):
                self.root = aux
            else:
                if (parent.right == pointer):
                    parent.right = aux
                else:
                    parent.left = aux
            #recalcular la lista de desbalances
            unbalances = self.calculate_ascendance(pointer)
            
    def calculate_node_balance (self, node: Node = None) -> int:
        if node is not None:
            return self.height(node.right) - self.height(node.left)
        return 0
    
    def calculate_ascendance (self, node: Node) -> list:
        unbalances = []
        while node is not None:
            node.balance = self.calculate_node_balance(node)
            if abs(node.balance) == 2:
                unbalances.append(node)
            node = self.search(node.key)[1]
        return unbalances

    def print_balances_inorder (self, node):
        if node is not None:
            self.print_balances_inorder(node.left)
            node.balance = self.calculate_node_balance(node)
            print("balance " + str(node.key) + ": " + str(node.balance))
            self.print_balances_inorder(node.right)
            
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
            
    def levels(self, node:Node, queue = []) -> None:
        if node is not None:
            queue.append(node)
        
        if len(queue) > 0 :
            tmp = queue.pop(0)
            print(tmp.key)

            if tmp.left is not None:
                queue.append(tmp.left)

            if tmp.right is not None:
                queue.append(tmp.right)
            
            self.levels( None, queue )
            
    # Utilidades ======================================================

    def test_tree(self):
        movies = [
            Movie("Mission: Impossible II", 546388108, 215409889, 39.4, 330978219, 60.6, 2000),
            Movie("Gladiator", 460583960, 187705427, 40.8, 272878533, 59.2, 2000),
            Movie("Cast Away", 429632142, 233632142, 54.4, 196000000, 45.6, 2000),
            Movie("What Women Want", 374111707, 182811707, 48.9, 191300000, 51.1, 2020),
            Movie("Dinosaur", 349822765, 137748063, 39.4, 212074702, 60.6, 2000),
            Movie("How the Grinch Stole Christmas", 345842198, 260745620, 75.4, 85096578, 24.6, 2000),
            Movie("Meet the Parents", 330444045, 166244045, 50.3, 164200000, 49.7, 2010),
            Movie("The Perfect Storm", 328718434, 182618434, 55.6, 146100000, 44.4, 2021),
            Movie("X-Men", 296339528, 157299718, 53.1, 139039810, 46.9, 2000),
            Movie("What Lies Beneath", 291420351, 155464351, 53.3, 135956000, 46.7, 2011),
        ]
        
        for movie in movies:
            self.insert(movie)
        return self
    
    def filter_by(self, flairs: str) :
        if " OR AND " in flairs or " AND OR " in flairs:
            print('Que te pasa animal')
            return []

        spec_year: int = None
        spec_min_income: float = None
        
        # Extraer los datos desde los flairs
        try:
            if "year:" in flairs:
                spec_year = int(flairs.split("year:")[1].split()[0])

            if "min:" in flairs:
                spec_min_income = float(flairs.split("min:")[1].split()[0])
                
        except ValueError:
            print("Not found or bad input")
            return []

        if "loved:true" in flairs:
            loved = True
        elif "loved:false" in flairs:
            loved = False
        else:
            loved = None
        
        # Inicializar el arbol con los noditos filtrados
        filtered_tree = AVLTree()
        
        # Funcion (dentro de funcion wiii) para filtrar nodos 💫 r e c u r s i v a m e n t e 💫
        def _filter_nodes(node):
            if node is None:
                return None

            # Extraer la informacion del nodo
            m_year = node.data.year
            m_income = node.data.foreign_earnings
            m_loved = node.data.domestic_percent_earnings >= node.data.foreign_percent_earnings
            
            # Evaluar condiciones
            year_chk = (spec_year is None or m_year >= spec_year)
            income_chk = (spec_min_income is None or m_income >= spec_min_income)
            loved_chk = True if loved is None else (m_loved == loved)

            # Aplicar la lógica para operandos OR y AND  
            if " OR " in flairs:
                if year_chk or income_chk and loved_chk:
                    filtered_tree.insert(node.data)
            elif " AND " in flairs:
                if year_chk and income_chk and loved_chk:
                    filtered_tree.insert(node.data)
                    
            # En caso tal no se especifique o no se encuentre un operando 
            else:
                if year_chk and income_chk and loved_chk:
                    filtered_tree.insert(node.data)

            # Llamado para subarboles izq y der
            _filter_nodes(node.left)
            _filter_nodes(node.right)
            
        # Ejecutar el primer recorrido
        _filter_nodes(self.root)
        
        return filtered_tree
    
    def search_by_title(self, query:str) -> 'AVLTree':
        filtered = AVLTree()

        # Un poquito mas de lo mismo que se hizo abajo con el filter by :)
        def _filter_nodes(node: Node):
            if node is None:
                return

            if query and node.data.title:
                if query.lower() in node.data.title.lower():
                    filtered.insert(node.data)

            _filter_nodes(node.left)
            _filter_nodes(node.right)
    
        _filter_nodes(self.root)
        return filtered
    
    def head(self, amount:int=10):
        out = AVLTree()

        if self.root is None:
            return out

        queue = []
        queue.append(self.root)
        count = 0

        while queue and count < amount:
            node = queue.pop(0)
            out.insert(node.data)
            count += 1

            if node.left and count < amount:
                queue.append(node.left)
            if node.right and count < amount:
                queue.append(node.right)
        
        return out

    def __repr__(self):
        return self.__print_tree(self.root)

    def __print_tree(self, node, level=0, side="root"):
        if node is None:
            return ""
        
        indent = " " * 4 * level

        # Define colors
        color_reset = "\033[0m"
        color_root = "\033[1;32m"    
        color_left = "\033[1;34m"    
        color_right = "\033[1;31m"   
        color_title = "\033[1;37m"   

        if side == "root":
            result = f"{indent}{color_root}(root){color_reset} -> {color_title}{node.data.title}{color_reset}\n"
        elif side == "left":
            result = f"{indent}{color_left}(left){color_reset} -> {color_title}{node.data.title}{color_reset}\n"
        else:  # right
            result = f"{indent}{color_right}(right){color_reset} -> {color_title}{node.data.title}{color_reset}\n"
        
        result += self.__print_tree(node.left, level + 1, "left")
        result += self.__print_tree(node.right, level + 1, "right")
        
        return result
    
    def to_dict(self):
        return {"root": self.__dict(self.root)}
    
    def __dict(self, node:Node):
        if node is None:
            return None
        
        return {
            "data": node.data.title,
            "balance": node.balance,
            "left": self.__dict(node.left),
            "right": self.__dict(node.right)
        }