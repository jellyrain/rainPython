import threading


def decorator(func, *args, **kwargs):
    """ 计时功能的装饰器 """

    def wrapper():
        if args and kwargs:
            func(*args, **kwargs)
        elif args:
            func(*args)
        elif kwargs:
            func(**kwargs)
        else:
            func()

    return wrapper


def thread(func, *args, **kwargs):
    """ 多线程运行 """

    def wrapper():
        if args and kwargs:
            threading.Thread(target=func, args=args, kwargs=kwargs).start()
        elif args:
            threading.Thread(target=func, args=args).start()
        elif kwargs:
            threading.Thread(target=func, kwargs=kwargs).start()
        else:
            threading.Thread(target=func).start()

    return wrapper


__all__ = ['decorator', 'thread']
