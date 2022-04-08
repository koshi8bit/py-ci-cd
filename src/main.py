from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a = "fafakjaljdfjkdsjfsdjfjsdfklsdfasfjdfjsgljsfgljdflgdkfgjdkfgldkfgkdfklgjldfjgkldjklfgjdklfjgkdjflkgldkfgjkldfjgkdlfgdkfgldkfjgldkfjgkldfjgkld"
    print(a)
    return "Hello world1"


if __name__ == '__main__':
    app.run()
