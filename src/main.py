from models import *

if __name__ == '__main__':
    print("----- Sample tree vacío -----")
    sample_tree = AVLTree()
    print(sample_tree.root)
    elements = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
    for i in elements:
        print("----- insert " + str(i) + "-----")
        print(sample_tree.insert(Movie(i,0,0,0,0,0,0)))
        sample_tree.inorder(sample_tree.root)
        print()

    elements = ["a","d","e","g","h","j","l","n"]
    for i in elements:
        print("----- delete " + str(i) + "-----")
        print(sample_tree.delete(i))
        sample_tree.inorder(sample_tree.root)
        print()