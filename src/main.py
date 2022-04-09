from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    a = "long_line long_line long_line long_line long_line long_line long_line long_line long_line long_line " \
        "long_line long_line long_line long_line long_line "
    print(a)
    return "Hello world"


if __name__ == '__main__':
    app.run()
