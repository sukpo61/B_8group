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


@app.route("/comment", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    person_receive = request.form['person_give']

    doc = {'name': name_receive,
           'comment': comment_receive,
           'person': person_receive}

    db.collection.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.collection.find({}, {'_id': False}))

    return jsonify({'comments': comment_list})



    # 명준 댓글

@app.route("/kimm_comment", methods=["POST"])
def kimm_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive,
           'comment': comment_receive}
    db.kimm_comments.insert_one(doc)

    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/kimm_comment", methods=["GET"])
def kimm_comment_get():
    kimm_comment_list = list(db.kimm_comments.find({}, {'_id': False}))

    return jsonify({'kimm_comments': kimm_comment_list})


#
#         # 희령 댓글
#
#
#
# @app.route("/yee_comment", methods=["POST"])
# def yee_comment_post():
#     name_receive = request.form['name_give']
#     comment_receive = request.form['comment_give']
#
#     doc = {'name': name_receive, 'comment': comment_receive}
#     db.yee_comments.insert_one(doc)
#
#     return jsonify({'msg': '방명록 남기기 완료!'})
#
#
# @app.route("/yee_comment", methods=["GET"])
# def yee_comment_get():
#     yee_comment_list = list(db.yee_comments.find({}, {'_id': False}))
#     return jsonify({'comments': yee_comment_list})
#
#
#     # 원준 댓글
#
#
# @app.route("/kimw_comment", methods=["POST"])
# def kimw_comment_post():
#     name_receive = request.form['name_give']
#     comment_receive = request.form['comment_give']
#
#     doc = {'name': name_receive,
#            'comment': comment_receive}
#     db.kimw_comments.insert_one(doc)
#
#     return jsonify({'msg': 'POST 연결 완료!'})
#
#
# @app.route("/kimw_comment", methods=["GET"])
# def kimw_comment_get():
#     kimw_comment_list = list(db.kimw_comments.find({}, {'_id': False}))
#
#     return jsonify({'kimw_comments': kimw_comment_list})
#
#
#
#
#     # 마리 댓글
#
# @app.route("/mari_comment", methods=["POST"])
# def mari_comment_post():
#     name_receive = request.form['name_give']
#     comment_receive = request.form['comment_give']
#
#     doc = {'name': name_receive,
#            'comment': comment_receive}
#     db.mari_comments.insert_one(doc)
#
#     return jsonify({'msg': 'POST 연결 완료!'})
#
#
# @app.route("/mari_server", methods=["GET"])
# def mari_comment_get():
#     mari_comment_list = list(db.mari_comments.find({}, {'_id': False}))
#
#     return jsonify({'mari_comments': mari_comment_list})
#



if __name__ == '__main__':
    app.run('0.0.0.0', port=5020, debug=True)