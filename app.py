from flask import Flask
from admin import admin

app = Flask(__name__)

app.register_blueprint(admin,url_prefix="/admin/")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run(debug=True)