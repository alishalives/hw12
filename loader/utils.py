import json

from main.utils import read_posts

# Создаем множество расширений, позволенных при загрузке изображения
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def save_picture(picture):
    extension = picture.filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        picture.save(f"./uploads/{picture.filename}")
        return f"/uploads/{picture.filename}"
    else:
        return


def save_to_json(posts_file, picture, content):
    post = {'pic': save_picture(picture), 'content': content}
    posts = read_posts(posts_file)
    posts.append(post)
    with open(posts_file, 'w', encoding="utf-8") as file:
        json.dump(posts, file)
