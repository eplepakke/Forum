from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def home_page():
    return render_template('Home_Page.html')


def main():
    db_session.global_init("db/forum.sqlite")
    app.run()


if __name__ == '__main__':
    main()
