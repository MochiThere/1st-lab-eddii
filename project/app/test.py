from models import *

if __name__ == '__main__':
    sample = AVLTree().test_tree()
    print(sample)
    print("============================================================")
    filtered = sample.search_and_filter("min:146100000")
    print(filtered)