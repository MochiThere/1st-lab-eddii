class Movie:
    def __init__(self, title: str, wwe: float, dome: float, dompe: float, fore: float, forpe: float, year: int):
        self.title: str = title
        self.wwide_earnings: float = wwe
        self.domestic_earnings: float = dome
        self.domestic_percent_earnings: float = dompe
        self.foreign_earnings: float = fore
        self.foreign_percent_earnings: float = forpe
        self.year: int = year