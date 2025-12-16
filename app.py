from flask import Flask
from database import init_db
from controller.note_api import note_api
from controller.note_web import note_web

app = Flask(__name__)

init_db()

app.register_blueprint(note_api)
app.register_blueprint(note_web)

if __name__ == "__main__":
    app.run(debug=True)
