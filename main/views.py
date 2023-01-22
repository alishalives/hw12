from flask import Blueprint, request, render_template
from main.utils import search_posts

# Создание нового Blueprint
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')


# Создание вьюшки основной страницы
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


# Создание вьюшки поиска
@main_blueprint.route('/search')
def search_page():
    search_input = request.args.get('s')
    posts = search_posts(search_input, "posts.json")
    return render_template('post_list.html', search_input=search_input, posts=posts)



