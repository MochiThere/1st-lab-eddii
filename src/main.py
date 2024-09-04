from models import *
from controllers import *

if __name__ == '__main__':
    sample = tree_from_csv('src/resources/dataset_movies.csv')
    print("\n\n============== Árbol Inicial ===================", end="\n\n")
    print(sample)
    tree_to_json(sample)
        
    
    
