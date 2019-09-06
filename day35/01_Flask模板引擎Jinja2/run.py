from flask  import  Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/bbs/')
def bbs():
    return  render_template('bbs.html')


@app.route('/blog/')
def blog():
    return  render_template('blog.html')
if __name__ == '__main__':
    app.run(port=5002)