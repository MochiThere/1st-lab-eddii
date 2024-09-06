import json
from ..models import Movie

def tree_to_json(tree, filename:str='data', path:str='project/app/static/resources'):
    data = tree.to_dict()
    with open(f'{path}/{filename}.json','w') as json_file:
        json.dump(data, json_file, indent=4)

def json_to_tree(tree, filename:str='data', path:str='project/app/static/resources'):
    with open(f'{path}/{filename}.json', 'r') as json_file:
        data = json.load(json_file)
    
    tree.root = __rebuild_tree(data)

def __rebuild_tree(node):
    if node is None:
        return None
    
    movie = node['data']