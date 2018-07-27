import json
import requests

TOKEN = "674400860:AAEU3jCSWBTQ86oDiDwagVL2EFOA2og6qUs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    message = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return message, chat_id


def send_message(message, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(message, chat_id)
    get_url(url)


text, chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)
