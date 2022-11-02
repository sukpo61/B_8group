from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.1xtz0yo.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route("/mari")
def mari():
    return render_template('mari.html')


@app.route("/mari", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.marina.insert_one(doc)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/mari", methods=["GET"])
def homework_get():
    comment_list = list(db.mari.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5022, debug=True)