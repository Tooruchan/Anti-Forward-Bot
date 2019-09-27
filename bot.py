from pyrogram import Client, Filters
import json

token = ""
api_id = ""
api_hash = ""
_channels = []
_conf = dict()


def load_channels():
    global _channels
    a = dict()
    with open("channels.json", encoding="utf-8") as f:
        a = json.load(f)
        f.close()
    _channels = a['channels']

def load_conf():
    global _conf
    with open("config.json",encoding="utf-8") as f:
        _conf = json.load(f)

load_channels()
load_conf()
print(_conf)
token = _conf['api_token']
print(token)
api_id = _conf['api_id']
print(api_id)
api_hash = _conf['api_hash']
print(api_hash)
app = Client("bot",bot_token=token,api_id=str(api_id),api_hash=str(api_hash))
# app = Client("bot",bot_token=token,api_id=str(api_id),api_hash=str(api_hash),proxy=dict(hostname="127.0.0.1",port=1080))
@app.on_message(Filters.group)
# 来自群组内部的消息
def check_message(client,message):
    try:
        channelid = message.forward_from_chat.id
    except:
        channelid = 0
    usrid = message.from_user.id
    usrfname = message.from_user.first_name
    if channelid in _channels:
        client.delete_messages(chat_id=message.chat.id,message_ids=message.message_id)
        client.send_message(chat_id=message.chat.id,text="["+usrfname+"](tg://user?id="+str(usrid)+") :\n"+"你刚才所转发的消息来源频道在本群不受允许。",parse_mode='markdown')
    else:
        print(message)

app.run()

