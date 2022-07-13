from flask import Flask, render_template
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('54.180.83.94', 27017, username="test", password="test")
db = client.recipes

@app.route('/')
def home():
   recipes_list = list(db.recipe.find({}, {'_id': False}))
   return render_template('main.html', recipes_list=recipes_list)


@app.route('/main/<category>', methods=['GET'])
def main(category):
    # print(category)
    if category == "all":
        recipes_list = list(db.recipe.find({ }, {'_id': False}))
    else:
        recipes_list = list(db.recipe.find({'food': category}))
        #print(recipes_list)
    return render_template("main_"+category+".html", recipes_list=recipes_list)

@app.route('/detail/<board_id>', methods=['GET'])
def detail(board_id):
    print(board_id)
    recipes = list(db.recipe.find({'id': board_id}))
    print(recipes)
    return render_template("detail.html", recipes=recipes)



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)