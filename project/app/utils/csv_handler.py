from ..models import *
from csv import reader

csv_path = "project/app/static/resources/dataset_movies.csv"

def search_in_csv(title: str) -> tuple[bool, list[Movie]]:
    movies = []
    
    with open(csv_path, "r", encoding='utf-8') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)  
        
        for row in csv_reader:
            if title.strip().lower() in row[0].strip().lower():
                movie = Movie(
                    title=row[0],
                    wwe=float(row[1]),
                    dome=float(row[2]),
                    dompe=float(row[3]),
                    fore=float(row[4]),
                    forpe=float(row[5]),
                    year=int(row[6])
                )
                movies.append(movie)
    
    return (False, []) if not movies else (True, movies)

def csv_head(base: int = 0, path: str = csv_path) -> list[Movie]:
    from random import randint
    #Numero aleatorio con nombre cuestionable usado como inicio del head
    wasa = randint(2, 4000-base)
    
    with open(path, 'r', encoding='utf-8') as csv_file:
        csv_reader = list(reader(csv_file))[wasa:wasa+base] 
        
        movies = [Movie(
            title=row[0],
            wwe=float(row[1]),
            dome=float(row[2]),
            dompe=float(row[3]),
            fore=float(row[4]),
            forpe=float(row[5]),
            year=int(row[6])
        ) for row in csv_reader]
        
        return movies
