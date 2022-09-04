# Импортирт библиотек
import logging
from flask import Blueprint, request, render_template
from json import JSONDecodeError
from functions import save_picture, add_post

# Перенаправление логов в файл logInfo.log
logging.basicConfig(filename="logInfo.log", level=logging.INFO, encoding='utf-8')

# Создание нового блюпринта
load_blueprint = Blueprint('load_blueprint', __name__, template_folder='templates')


# Создание вьюшки
@load_blueprint.route('/post')
def load_post():
    return render_template('post_form.html')


@load_blueprint.route('/post', methods=['POST'])
def page_add_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    # Обработка ошибок
    if not picture or not content:
        return "Нет изображения и/или описания"

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info("Неверное расширение файла\n ***********")
        return "Неверное расширение файла"

    # Обработка ошибок
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл некорректен"

    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
