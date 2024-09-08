class Movie:
    def __init__(self, title: str, wwe: float, dome: float, dompe: float, fore: float, forpe: float, year: int):
        self.title: str = title
        self.worldwide_earnings: float = wwe
        self.domestic_earnings: float = dome
        self.domestic_percent_earnings: float = dompe
        self.foreign_earnings: float = fore
        self.foreign_percent_earnings: float = forpe
        self.year: int = year
    
    def to_dict(self):
        return {
            "title": self.title,
            "worldwide": self.worldwide_earnings,
            "domestic": self.domestic_earnings,
            "domestic_percent": self.domestic_percent_earnings,
            "foreign": self.foreign_earnings,
            "foreign_percent": self.foreign_percent_earnings,
            "year": self.year
        }
    
    def __repr__(self) -> str:
        return self.title
    
    @staticmethod
    def from_dict(movie_dict:dict):
        return Movie(
            title=movie_dict['title'],
            wwe=float(movie_dict['worldwide']),
            dome=float(movie_dict['domestic']),
            dompe=float(movie_dict['domestic_percent']),
            fore=float(movie_dict['foreign']),
            forpe=float(movie_dict['foreign_percent']),
            year=int(movie_dict['year'])
        )