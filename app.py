# Импортирт библиотек
from flask import Flask, send_from_directory
from loader.loader_view import load_blueprint
from main.main_view import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрация блюипринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(load_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
