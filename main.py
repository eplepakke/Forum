from flask import Flask, render_template, request
from data import db_session
from data.news import News
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def home_page():
    session = db_session.create_session()
    news = session.query(News)
    return render_template('Home_Page.html', news=news)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'])
        user.set_password(request.form['password'])
        session = db_session.create_session()
        session.add(user)
        session.commit()
        return "<a class='link' href='index'>Назад на главную</a>"


@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.method == 'GET':
        return render_template('auth.html')
    elif request.method == 'POST':
        request.form['name']
        return "<a class='link' href='index'>Назад на главную</a>"


def main():
    db_session.global_init("db/forum.sqlite")
    app.run()


if __name__ == '__main__':
    main()
