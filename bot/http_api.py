import requests


def get(url, params=None) -> requests.Response:
    return requests.get(url, params=params)


def post(url, data=None) -> requests.Response:
    return requests.post(url, data=data)


def send_private_msg(host: str, port: int, user_id: int, message: str) -> requests.Response:
    """发送私聊消息"""
    url = f'http://{host}:{str(port)}/send_private_msg'
    params = {
        'user_id': user_id,
        'message': message
    }
    return requests.get(url, params=params)


def send_group_msg(host: str, port: int, group_id: int, message: str) -> requests.Response:
    """发送群消息"""
    url = f'http://{host}:{str(port)}/send_group_msg'
    params = {
        'group_id': group_id,
        'message': message
    }
    return requests.get(url, params=params)


def set_group_kick(host: str, port: int, group_id: int, user_id: int) -> requests.Response:
    """群组踢人"""
    url = f'http://{host}:{str(port)}/set_group_kick'
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    return requests.get(url, params=params)


def set_group_ban(host: str, port: int, group_id: int, user_id: int) -> requests.Response:
    """群组禁言"""
    url = f'http://{host}:{str(port)}/set_group_ban'
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    return requests.get(url, params=params)


def set_group_whole_ban(host: str, port: int, group_id: int, enable: bool) -> requests.Response:
    """群组全员禁言"""
    url = f'http://{host}:{str(port)}/set_group_whole_ban'
    params = {
        'group_id': group_id,
        'enable': enable
    }
    return requests.get(url, params=params)


def get_group_at_all_remain(host: str, port: int, group_id: int) -> requests.Response:
    """获取群组at所有人剩余次数"""
    url = f'http://{host}:{str(port)}/get_group_at_all_remain'
    params = {
        'group_id': group_id
    }
    return requests.get(url, params=params)


__all__ = ['get', 'post', 'send_private_msg', 'send_group_msg', 'set_group_kick', 'set_group_ban', 'set_group_whole_ban', 'get_group_at_all_remain']
