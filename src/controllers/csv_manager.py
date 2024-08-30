from ..models.node import Node
from ..models.avltree import AVLTree
from ..models.movie import Movie
from csv import reader, writer

class Csv_manager():
    
    def __init__(self, file_src: str) -> None:
        self.file_src: str = file_src
        
    def generate_tree_from_csv(self, tree: AVLTree) -> Node:
        with open(self.file_src, "r") as csv_file:
            file_reader = reader(csv_file)
            for i in file_reader:
                tree.insert(Movie(i))
            return tree.root