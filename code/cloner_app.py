from flask import Flask, render_template, request, redirect
app = Flask(__name__)

REPO = '--------- WWW ---------'


@app.route('/')
def index():
    return render_template('main.html', repo=REPO)


@app.route('/clone', methods=['POST'])
def clone():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
