from flask import Flask, request
from bot.message import Message
from bot.with_message import add_function, with_message
from bot.http_api import send_private_msg, send_group_msg, set_group_kick, set_group_ban, set_group_whole_ban, get_group_at_all_remain


class QQBot:
    def __init__(self, host: str = '0.0.0.0', port: int = 5701, bot_host: str = '127.0.0.1', bot_port: int = 5700):
        self.host = host
        self.port = port
        self.bot_host = bot_host
        self.bot_port = bot_port
        self.app = Flask(__name__)

    def add_function(self, func: callable) -> 'QQBot':
        """添加消息处理函数 能得到的参数有 message 和 message_type"""
        add_function(func)
        return self

    def run(self):
        """启动服务"""
        @self.app.route('/', methods=["POST"])
        def index():
            data = request.get_json()
            if data['post_type'] == 'meta_event':
                return 'True'
            msg = Message(data)
            with_message(msg, msg.__class__.__name__, self.bot_host, self.bot_port)
            return 'True'

        self.app.run(host=self.host, port=self.port)


version = '1.0.0'
