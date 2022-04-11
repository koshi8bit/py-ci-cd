from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    a = "long_line long_line long_line long_line long_line long_line long_line long_line long_line long_line " \
        "long_line long_line long_line long_line long_line "
    print(a)
    return "Hello world"


@app.route("/api/v1/foo")
def api_v1_foo():
    return "bar SEXY 999 567"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
