from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Talha')

# @app.route('/<name>', methods = ['GET'])
# def greet(name):
#     return render_template('greet.html', user = name)

@app.route('/greet', methods = ['GET'])
def greet():
    if 'user' in request.args:
        usr = request.args['user']
        return render_template('greet.html', user = usr)
    else:
        return render_template('greet.html', user = 'Send your user name with "user" parameter in query string')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        return render_template('secure.html', user = user_name)
    else:
        return render_template('login.html', )


if __name__ == '__main__':
    # app.run('0.0.0.0', port=80, debug=True)
    app.run(debug=True)
