from flask import Blueprint, render_template, request, jsonify
from ..models import *

main = Blueprint('main', __name__)

@main.route('/profiles')
def profiles():
    return render_template('profiles.html')

@main.route('/browse', methods=['GET', 'POST'])
def main_page():
    sample: AVLTree = AVLTree.test_tree() 

    if request.method == 'POST':
        query = request.form.get('text-area')

        filtered_sample = sample.search_by_title(query)
        print(filtered_sample)

        return jsonify(filtered_sample.to_dict())
    
    else:
        print("didn't entered")
        return render_template('main-page.html')

@main.route('/my-list')
def my_list():
    return render_template('my-list.html')