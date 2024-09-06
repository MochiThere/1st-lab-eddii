from models.movie import Movie
from csv import reader
    
csv_path = "project/app/static/resources/dataset_movies.csv"

def search_in_csv (title: str) -> tuple[bool, Movie]:
    with open(csv_path, "r") as csv_file:
        read = reader(csv_file)
        next(read)
        for i in read:
            if (i[0] == title):
                return True, Movie(i[0], float(i[1]), float(i[2]), float(i[3]), float(i[4]),float(i[5]), int(i[6]))
        csv_file.close()
        return False, None

def csv_head(base: int = 0, path:str=csv_path) -> list:
    with open(path, "r") as csv_file:
        read = reader(csv_file)
        next(read) 
        
        if base == 0:
            return [next(read)[0]] 
        
        return [next(read)[0] for _ in range(base)]
