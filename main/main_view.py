# Импортирт библиотек
import logging
from flask import Blueprint, request, render_template
from json import JSONDecodeError
from functions import get_posts_by_word

# Перенаправление логов в файл logInfo.log
logging.basicConfig(filename="logInfo.log", level=logging.INFO, encoding='utf-8')

# Создание нового блюпринта
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создание вьюшки
@main_blueprint.route("/")
def index_page():
    return render_template('index.html')


@main_blueprint.route("/search/")
def search_page():
    search_query = request.args.get("s", '')
    # Обработка ошибок
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла. Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        logging.error("Ошибка загрузки файла. Файл некорректный")
        return "Файл некорректный"
    logging.info(f"Поиск по слову '{search_query}'")
    return render_template('post_list.html', search=search_query, posts=posts)
