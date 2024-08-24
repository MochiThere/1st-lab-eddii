from typing import Optional, Any
from Movie import Movie

class Node:

    def __init__(self, data: Optional[Any] = None) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0
        
        