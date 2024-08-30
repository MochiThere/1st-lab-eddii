from .movie import Movie

class Node:

    def __init__(self, data: Movie= None) -> None:
        self.key: str = data.title
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.balance: int = 0
        
        