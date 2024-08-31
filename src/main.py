from models import *

if __name__ == '__main__':
    print("----- Sample tree vacío -----")
    sample_tree = AVLTree()
    print(sample_tree.root)
    elements = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
    for i in elements:
        print("----- insert " + str(i) + "-----")
        print(sample_tree.insert(Movie([i,0,0,0,0,0,0])))
        sample_tree.inorder(sample_tree.root)
        print()

    elements = ["a","l","n"]
    for i in elements:
        print("----- delete " + str(i) + "-----")
        print(sample_tree.delete(i))
        sample_tree.levels(sample_tree.root)
        print()

    threehead = sample_tree.head(15)
    for head in threehead:
        print(head.key, end=" ")
    print()