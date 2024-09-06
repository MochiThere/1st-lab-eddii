from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from ..models import *
from ..utils import *

main = Blueprint('main', __name__)

@main.route('/profiles')
def profiles():
    return render_template('profiles.html')

@main.route('/browse', methods=['GET', 'POST'])
def main_page():
    sample: AVLTree = AVLTree().test_tree() 

    if request.method == 'POST':
        query = request.form.get('text-area')

        filtered_sample = search_in_csv(query)[1]
        print(f'\033[1;32m{filtered_sample}\033[0m')

        session['results'] = filtered_sample

        return redirect(url_for('main.explore'))
    else:
        print("didn't entered")
        return render_template('main-page.html')

@main.route('/my-list')
def my_list():
    return render_template('my-list.html')

@main.route('/explore')
def explore():
    results = session.get('results', [])

    return render_template('explore.html', results= results)