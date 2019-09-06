from flask import Flask, render_template, flash
from flask_bootstrap import  Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'WESTOS'
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    flash('login success')
    return  render_template('index.html')

@app.route('/bbs/')
def bbs():
    return  render_template('bbs.html')


@app.route('/blog/')
def blog():
    return  render_template('blog.html')

if __name__ == '__main__':
    app.run(port=5003)