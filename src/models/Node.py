from typing import Optional

class Node:

    def __init__(self, data: Optional[str] = None) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0
        
        