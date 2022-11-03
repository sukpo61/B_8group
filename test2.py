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

