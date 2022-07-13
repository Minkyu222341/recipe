from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('3.35.218.47', 27017, username="test", password="test")
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/add', methods=["GET"])
def add_page():
    return render_template('add.html')

@app.route('/update', methods=["GET"])
def update_page():
    write_data = list(db.testDB.find({}, {'_id': False}))
    return render_template('update.html',write_data=write_data)

@app.route('/update', methods=["POST"])
def updatePost():
    title_receive = request.form.get("title", type=str)
    author_receive = request.form.get("author", type=str)
    url_receive = request.form.get("url", type=str)
    food_receive = request.form.get("food", type=str)
    content_receive = request.form.get("content", type=str)
    print(title_receive,author_receive)
    db.testDB.update_one({'author':title_receive},{'$set':{'title':author_receive}})
    return render_template("main.html")


@app.route("/add", methods=["POST"])
def addPost():
    title_receive = request.form.get("title", type=str)
    author_receive = request.form.get("author", type=str)
    url_receive = request.form.get("url", type=str)
    food_receive = request.form.get("food", type=str)
    content_receive = request.form.get("content", type=str)
    print(title_receive,author_receive,url_receive,food_receive,content_receive)
    doc={
        'title':title_receive,
        'author':author_receive,
        'url': url_receive,
        'food':food_receive,
        'content':content_receive
    }
    db.testDB.insert_one(doc)

    return render_template("main.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)