from typing import Union
from bot.message import Message_Group, Message_Private

function_list = []


def with_message(message: Union[Message_Group, Message_Private], message_type: str, host: str, port: int) -> None:
    if function_list:
        for func in function_list:
            func(message, message_type, host, port)


def add_function(func: callable) -> None:
    function_list.append(func)


__all__ = ['add_function', 'with_message']
