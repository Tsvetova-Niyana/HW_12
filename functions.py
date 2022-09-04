import json
import logging

POST_PATH = "posts.json"


def load_posts() -> list[dict]:
    """Загрузка данных из файла .json"""
    with open(POST_PATH, encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    """Получение списка постов в соответствии с критериями поиска"""
    result_post = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result_post.append(post)
    return result_post


def save_picture(picture) -> str:
    """Сохранение изображения под собственным именем в папке ./uploads/images/"""
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def add_post(post: dict) -> dict:
    """Добавление поста в файл .json"""
    posts = load_posts()
    posts.append(post)

    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
