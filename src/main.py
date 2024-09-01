from models import *
from controllers import *

if __name__ == '__main__':
    arbolito = AVLTree().test_tree()
    print("\n\n============== Arbol Inicial ===================", end="\n\n")
    print(arbolito)
    print("============== Arbol > 2020 ===================", end="\n\n")
    print(arbolito.filter_by("year:2020"))
    print("============== Arbol > 164200000 ===================", end="\n\n")
    print(arbolito.filter_by("min:164200000"))
    print("============== Arbol ambos criterios ===============", end="\n\n")
    print(arbolito.filter_by("year:2020 AND min:164200000"))
    print("============== Arbol uno u ambos criterios ===========", end="\n\n")
    print(arbolito.filter_by("year:2020 OR min:164200000"))
    
    tree_to_json(arbolito)