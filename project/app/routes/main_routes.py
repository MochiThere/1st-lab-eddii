from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from ..models import *
from ..utils import *

main = Blueprint('main', __name__)
temp_tree = AVLTree()


@main.route('/profiles')
def profiles():
    return render_template('profiles.html')

@main.route('/browse', methods=['GET', 'POST'])
def main_page():
    sample: AVLTree = AVLTree().test_tree() 

    if request.method == 'POST':
        query = request.form.get('text-area')

        filtered_sample = [movie.to_dict() for movie in search_in_csv(query)[1]]
        print(f'\033[1;32m{filtered_sample}\033[0m',end="\n")

        session['results'] = filtered_sample

        return redirect(url_for('main.explore'))
    else:
        print("didn't entered")
        return render_template('main-page.html')

@main.route('/my-list', methods=['GET', 'POST'])
def my_list():
    if request.method == 'POST':
        data = request.json
        action = data.get('action')
        movie_title = data.get('title')

        if action == 'delete' and movie_title:
            print(f'Borrando: {movie_title}')
            res = temp_tree.delete(movie_title)
            tree_to_json(temp_tree)


            if res:
                return jsonify({'success': True, 'message': f'Movie {movie_title} deleted successfully'}), 200
            else:
                return jsonify({'success': False, 'message': f'Movie {movie_title} not found'}), 404

        else:
            movie_obj = Movie.from_dict(data)
            temp_tree.insert(movie_obj)
            tree_to_json(temp_tree)


    return render_template('my-list.html')


@main.route('/explore')
def explore():
    results = session.get('results', [])

    return render_template('explore.html', results= results)