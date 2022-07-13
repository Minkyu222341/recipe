from flask import Flask, render_template, request, jsonify ,redirect
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('3.35.218.47', 27017, username="test", password="test")
db = client.dbsparta_plus_week1


@app.route('/')
def home():
    posts = list(db.board.find({}, {'_id': False}))
    # print(len(posts))
    print(posts)
    return render_template('main.html',recipes_list=posts)

@app.route('/detail/<board_id>', methods=['GET'])
def detail(board_id):
    print(board_id)
    board = list(db.board.find({'index': board_id}))
    return render_template("detail.html", recipes=board)

@app.route('/add', methods=["GET"])
def add_page():
    return render_template('add.html')

@app.route('/update/<board_id>', methods=["GET"])
def update_page(board_id):
    write_data = list(db.board.find({'index': board_id}))
    return render_template('update.html',write_data=write_data,index=board_id)

@app.route('/update', methods=["POST"])
def updatePost():
    title_receive = request.form.get("title", type=str)
    index_receive = request.form.get("index", type=str)
    url_receive = request.form.get("url", type=str)
    food_receive = request.form.get("catecory", type=str)
    content_receive = request.form.get("content", type=str)
    print(title_receive,index_receive)
    db.board.update_one({'index':index_receive},{'$set':{'title':title_receive}})

    return redirect("/")


@app.route("/add", methods=["POST"])
def addPost():
    posts = list(db.board.find({}))
    index = str(len(posts)+1)
    title_receive = request.form.get("title", type=str)
    author_receive = request.form.get("author", type=str)
    url_receive = request.form.get("url", type=str)
    category_receive = request.form.get("category", type=str)
    content_receive = request.form.get("content", type=str)
    print(title_receive,author_receive,url_receive,category_receive,content_receive)
    doc={
        'index':index,
        'title':title_receive,
        'url': url_receive,
        'author':author_receive,
        'category':category_receive,
        'content':content_receive
    }
    db.board.insert_one(doc)

    return redirect("/")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)