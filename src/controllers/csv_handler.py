from models.avltree import AVLTree
from models.movie import Movie
from csv import reader

def tree_from_csv(path:str) -> AVLTree:
    tree = AVLTree()
    with open(path, "r") as csv_file:
        read = reader(csv_file)
        next(read)
        for i in read:
            tree.insert(Movie(i[0], float(i[1]), float(i[2]), float(i[3]), float(i[4]),float(i[5]), int(i[6])))    
    return tree
            
