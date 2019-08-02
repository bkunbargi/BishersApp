from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug = True,threaded = True,use_reloader = False)
