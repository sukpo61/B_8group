from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:go3355@cluster0.vqsgnyr.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('main.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive,
           'comment': comment_receive}
    db.comments.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():

    fan_list = list(db.comments.find({}, {'_id': False}))

    return jsonify({'fans': fan_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)