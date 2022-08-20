from datetime import datetime


class Message_Group:
    def __init__(self, message: dict):
        self.sub_type = message['sub_type']
        self.message_id = message['message_id']
        self.message = message['message']
        self.sender = {'user_id': message['sender']['user_id'], 'nickname': message['sender']['nickname'],
                       'role': message['sender']['role']}
        self.time = datetime.fromtimestamp(message['time']).strftime("%Y-%m-%d %H:%M:%S")
        self.timestamp = message['time']
        self.self_id = message['self_id']
        self.group_id = message['group_id']


class Message_Private:
    def __init__(self, message: dict):
        self.sub_type = message['sub_type']
        self.message_id = message['message_id']
        self.message = message['message']
        self.sender = {'user_id': message['sender']['user_id'], 'nickname': message['sender']['nickname']}
        self.time = datetime.fromtimestamp(message['time']).strftime("%Y-%m-%d %H:%M:%S")
        self.timestamp = message['time']
        self.self_id = message['self_id']


def Message(message: dict) -> Message_Group or Message_Private:
    if 'group_id' in message.keys():
        return Message_Group(message)
    else:
        return Message_Private(message)


__all__ = ['Message', 'Message_Group', 'Message_Private']
