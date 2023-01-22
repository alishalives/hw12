import json
from flask import Blueprint, render_template, request
from loader.utils import save_picture, save_to_json

# Создание нового Blueprint
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')


# Создание вьюшек добавления поста
@loader_blueprint.route("/post")
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=['POST'])
def record():
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        return "Поля не заполнены полностью"

    result = save_picture(picture)
    if not result:
        return "Тип вложенного файла не поддерживается! Пожалуйста используйте только расширения png, jpg или jpeg"
    else:
        save_to_json('posts.json', picture, content)
    return render_template("post_uploaded.html", result=result, content=content)

