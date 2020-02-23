from flask import Flask, render_template, request
from data import make_comment, get_comment
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        fun = reversed(get_comment())
        return render_template('home.html', comment=fun)
    elif request.method == 'POST':
        make_comment()
        fun = reversed(get_comment())
        return render_template('home.html', comment=fun)


if __name__ == '__main__':
    app.run()
