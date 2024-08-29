from typing import Optional
from Movie import Movie

class Node:
    
    def __init__(self, data: Optional[Movie] = None) -> None:
        self.key: str = data.title
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.balance: int = 0
        
        