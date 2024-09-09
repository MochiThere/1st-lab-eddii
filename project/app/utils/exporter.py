import json

def tree_to_json(tree, filename:str='data', path:str='project/app/static/resources'):
    data = tree.to_dict()
    with open(f'{path}/{filename}.json','w') as json_file:
        json.dump(data, json_file, indent=4)