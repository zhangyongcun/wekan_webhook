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
    msg = ''
    if description == 'act-createCard':  # 添加卡片
        msg = '{} 添加卡片 {}'.format(user, card)
    if description == 'act-joinMember':  # 添加成员:
        msg = '{} 添加成员: {}'.format(user, text)
    if description == 'act-moveCard':  # 移动卡片
        msg = text.replace('Default', '').replace(' 到看板', '').replace(' 泳道', '').replace('Dev', '').replace('列表', '')
    if msg:
        cmd = './pushWechatMsg --msg "{}"'.format(msg)
        os.system(cmd)
    return jsonify({
        'code': 200,
        'msg': 'success'
    })


app.run(host="0.0.0.0", port=8080)
