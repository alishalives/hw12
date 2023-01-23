import json

from main.utils import read_posts

# Создаем множество расширений, позволенных при загрузке изображения
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Функция, сохраняющая изображение при правильном расширении
def save_picture(picture):
    extension = picture.filename.split(".")[-1]
    filename = picture.filename
    if extension in ALLOWED_EXTENSIONS:
        picture.save(f"./uploads/images/{filename}")
        return filename
    else:
        return


# Функция перезаписывает json файл с учетом нового поста
def save_to_json(posts_file, picture, content):
    post = {'pic': f"/uploads/images/{picture.filename}", 'content': content}
    posts = read_posts(posts_file)
    posts.append(post)
    with open(posts_file, 'w', encoding="utf-8") as file:
        json.dump(posts, file)
