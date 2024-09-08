from ..models import *
from csv import reader
    
csv_path = "project/app/static/resources/dataset_movies.csv"

def search_in_csv (title: str) -> tuple[bool, list[Movie]]:
    movies = []

    with open(csv_path, "r", encoding='utf-8') as csv_file:        
        csv_reader = reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if title.strip().lower() in row[0].strip().lower():
                movies.append(Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

    return (False, []) if len(movies) == 0 else (True, movies)
        

def csv_head(base: int = 0, path:str=csv_path) -> list:
    with open(path, "r") as csv_file:
        read = reader(csv_file)
        next(read) 
        
        if base == 0:
            return [next(read)[0]] 
        
        return [next(read)[0] for _ in range(base)]
