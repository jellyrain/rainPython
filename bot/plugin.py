from bot.message import Message_Group
from bot.http_api import get, send_group_msg


def menu(menu_str: str):
    def m(message: Message_Group, message_type: str, host: str, port: int) -> None:
        msg = message.message
        if msg.startswith('rain酱 功能表'):
            send_group_msg(host, port, message.group_id, menu_str)

    return m


def hello(message: Message_Group, message_type: str, host: str, port: int) -> None:
    msg = message.message
    if msg.startswith('rain酱 你好呀'):
        send_group_msg(host, port, message.group_id, f"{message.sender['nickname']} 你好呀！！！")


def song_163(message: Message_Group, message_type: str, host: str, port: int) -> None:
    msg = message.message
    if msg.startswith('rain酱 '):
        msg = msg[6:]
        if msg.startswith('点歌：'):
            msg = msg[3:]
            send_group_msg(host, port, message.group_id, '正在搜索歌曲...')
            song_id = get('https://music.cyrilstudio.top/search', {'keywords': msg}).json()['result']['songs'][0]['id']
            send_group_msg(host, port, message.group_id, f'[CQ:music,type=163,id={song_id}]')


def img(message: Message_Group, message_type: str, host: str, port: int) -> None:
    msg = message.message
    if msg.startswith('rain酱 涩图'):
        res = get('https://api.lolicon.app/setu/v2', {
            'num': 1
        }).json()['data'][0]
        send_group_msg(host, port, message.group_id,
                       f"图片名：{res['title']} 作者名：{res['author']}[CQ:image,file={res['urls']['original']}]")
