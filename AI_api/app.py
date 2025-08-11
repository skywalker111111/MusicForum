from flask import Flask, request, jsonify
from flask_cors import CORS
from baidu_util import baidu_api


app = Flask(__name__)
CORS(app, origins=["http://localhost:8060"])

@app.route('/api/get_response', methods=['POST'])
def get_response():
    user_query = request.json.get('prompt')  # 从请求中获取输入字符串
    if not user_query:
        return jsonify({'error': '请提供输入字符串'}), 400

    initial_prompt = "你是AveMusica音乐网站小助手，负责回答各种音乐方面的问题，你在回答时只返回纯文本，不用markdown格式，字数尽量控制在200字以内。"

    # 将用户查询与初始 prompt 合并
    full_prompt = f"{initial_prompt} 用户提问: {user_query}"
    # 调用文心一言 API
    response = baidu_api(full_prompt)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(port=8083)