from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    # if more than 120 symbols len -> Lint (code format guidelines check) fail
    a = "long_line long_line long_line long_line long_line long_line long_line long_line long_line long_line                   " \
        "long_line long_line long_line long_line long_line "
    print(a)
    return "Hello world"


@app.route("/api/v1/foo")
def api_v1_foo():
    return "bar"


@app.route("/api/v2/foo")
def api_v2_foo():
    return "sexy bar"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
