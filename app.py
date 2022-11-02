from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:go3355@cluster0.vqsgnyr.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/go')
def go():
    return render_template('go.html')

@app.route('/mari')
def mari():
    return render_template('mari.html')


@app.route('/yee')
def yee():
    return render_template('yee.html')

@app.route('/kimm')
def kimm():
    return render_template('kimm.html')

@app.route('/kimw')
def kimw():
    return render_template('kimw.html')


@app.route("/go_comment", methods=["POST"])
def go_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive,
           'comment': comment_receive}
    db.go_comments.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/go_comment", methods=["GET"])
def go_comment_get():
    go_comment_list = list(db.go_comments.find({}, {'_id': False}))

    return jsonify({'go_comments': go_comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5008, debug=True)