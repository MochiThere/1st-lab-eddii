from models import *
from controllers import *

if __name__ == '__main__':
    sample = tree_from_csv('E:/0. University/0. Github Repositories/1st-lab-eddii/src/resources/dataset_movies.csv').head(5)
    print("\n\n============== Árbol Inicial ===================", end="\n\n")
    print(sample)
        
    
    
