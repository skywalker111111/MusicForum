import requests
import json

baidu_AppID = '61014787'
baidu_AK = 'Bsc63dQhBqwAlAwJSYzklrdv'
baidu_SK = 'RqagN6rsIBRn12Z67Gm35PVGCDadBzUQ'


def baidu_api(prompt):
    """
    :param prompt: 输入字符串
    :return: 文心一言 API 的响应字符串
    """
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("result")


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": baidu_AK, "client_secret": baidu_SK}

    return str(requests.post(url, params=params).json().get("access_token"))