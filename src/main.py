from models import *
from controllers import *

if __name__ == '__main__':
    arbolito = AVLTree().test_tree()
    print("\n\n============== Arbol Inicial ===================", end="\n\n")
    print(arbolito)
    
    print("\n\n============== Arbol Filtrado ===================", end="\n\n")
    print(arbolito.search_and_filter("year:2020 AND min:164200000"))
    
    #tree_to_json(arbolito)