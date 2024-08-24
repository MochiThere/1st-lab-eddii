from typing import Any, Optional
class Movie():
    def __init__(self):
        self.title: str = None
        self.wwide_earnings: float = 0
        self.domestic_earnings: float = 0
        self.domestic_percent_earnings: float = 0
        self.foreign_earnings: float = 0
        self.foreign_percent_earnings: float = 0
        self.year: int = 0       