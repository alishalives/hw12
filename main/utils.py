import json


# Функция чтения JSON-файла
def read_posts(post):
    with open(post, 'r', encoding="utf-8") as file:
        posts = json.load(file)
        return posts


# Функция поиска постов, содержащих введенное пользователем строку в поиске
def search_posts(search_input, way):
    posts = []
    for post in read_posts(way):
        if search_input.lower() in post['content'].lower():
            posts.append(post)
    return posts
