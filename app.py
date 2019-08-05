from flask import Flask,render_template,request,jsonify
from Projects.tweeter import run_bot, run_analysis,respond_to,retweet
from Projects.Instabot import run_insta,image_handle,local_image
from Projects.crawler import run,responder

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



@app.route('/twitterbot',methods = ['POST'])
def twitterbot():
    if request.form['user_tweet'] != '' and request.form['responderhandle'] != ''  and request.form['statusid'] != '' :
        respond_to(request.form['responderhandle'],request.form['user_tweet'],request.form['statusid'])
        tweeted = request.form['user_tweet']
        return render_template('project.html')
    if request.form['user_tweet'] != '':
        tweeted = retweet(request.form['user_tweet'])
        return render_template('project.html')

@app.route('/twitterbot2',methods = ['POST'])
def twitterbot2():
    if request.form['keyword1'] != '':
        keyword1 = request.form['keyword1']
        tweeted_list = run_bot(keyword1)
        min_t,max_t = run_analysis(tweeted_list)
        return render_template('project.html')


@app.route('/instabot', methods=['POST'])
def instabot():
    photo_loc = "Projects/image_name.jpg"
    caption = request.form['caption']
    if request.form['tpic'] != '':
        photo_url = request.form['tpic']
        #req.urlretrieve(photo_url, photo_loc)
        run_insta(image_handle,photo_url, photo_loc,caption)
        #image_handle(photo_url,"Projects/image_name.jpg")
        return render_template('project.html')

    if request.files['file'] != '':
        photo = request.files['file']
        run_insta(local_image,photo,photo_loc,caption)
        #local_image(photo,"Projects/image_name.jpg")
        return render_template('project.html')


@app.route('/redditbot', methods=['POST'])
def redditbot():
    if request.form['subkey'] != '' and request.form['redditkeyword'] != '':
        sub_list = run(request.form['subkey'],request.form['redditkeyword'])
        return render_template('redditresults.html',result = sub_list)



@app.route('/redditbot2', methods=['POST'])
def redditbot2():
    if request.form['madecomment'] != '' and request.form['subid'] != '' and request.form['uresponse'] != '':
        made_comment = request.form['madecomment']
        sub_id = request.form['subid']
        u_response = request.form['uresponse']
        responder(sub_id,made_comment,u_response)
        return render_template('project.html')



if __name__ == '__main__':
    app.run(debug = True,threaded = True,use_reloader = False)
