class Movie:
    def __init__(self, csv_line: list[str]):
        self.title: str = csv_line[0]
        self.wwide_earnings: float = float(csv_line[1])
        self.domestic_earnings: float = float(csv_line[2])
        self.domestic_percent_earnings: float = float(csv_line[3])
        self.foreign_earnings: float = float(csv_line[4])
        self.foreign_percent_earnings: float = float(csv_line[5])
        self.year: int = int(csv_line[6])