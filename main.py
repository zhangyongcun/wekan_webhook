import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/wekan', methods=['POST'])
def hello():
    print(request.json)
    description = request.json.get('description')
    user = request.json.get('user')
    card = request.json.get('card')
    text = request.json.get('text')
    if description == 'act-createCard':  # 添加卡片
        msg = '{} 添加卡片 {}'.format(user, card)
    if description == 'act-joinMember':  # 添加成员:
        msg = '有新的任务卡片: {}'.format(text)
    if description == 'act-moveCard':  # 移动卡片
        if '完成' in text:
            msg = '完成: {}'.format(card)
        if '进行中' in text:
            msg = '进行中: {}'.format(card)
    cmd = './pushWechatMsg --msg "{}"'.format(msg)
    os.system(cmd)
    return jsonify({
        'code': 200,
        'msg': 'success'
    })


app.run(host="0.0.0.0", port=8080)
