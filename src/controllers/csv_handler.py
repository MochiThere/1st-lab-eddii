from models.avltree import AVLTree
from models.movie import Movie
from csv import reader
    
csv_path = "src/resources/dataset_movies.csv"
    
def tree_from_csv() -> AVLTree:
    tree = AVLTree()
    with open(csv_path, "r") as csv_file:
        counter = 0
        read = reader(csv_file)
        next(read)
        for i in read:
            tree.insert(Movie(i[0], float(i[1]), float(i[2]), float(i[3]), float(i[4]),float(i[5]), int(i[6])))   
            counter += 1
    tree = tree.head(counter)
    return tree

def search_in_csv (title: str) -> tuple[bool, Movie]:
    with open(csv_path, "r") as csv_file:
        read = reader(csv_file)
        next(read)
        for i in read:
            if (i[0] == title):
                return True, Movie(i[0], float(i[1]), float(i[2]), float(i[3]), float(i[4]),float(i[5]), int(i[6]))
        return False, None
