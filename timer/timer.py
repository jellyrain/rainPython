import schedule
import time

from timer.tools import decorator


class Timer_Interval:
    """ 间隔时间执行类 """

    def __init__(self, timer_name: str = 'Timer_Interval') -> None:
        self.id = timer_name

    def second(self, job: decorator, second: int = 1) -> 'Timer_Interval':
        """ 间隔多少秒执行一次 """
        schedule.every(second).seconds.do(job)
        return self

    def minute(self, job: decorator, minute: int = 1) -> 'Timer_Interval':
        """ 间隔多少分钟执行一次 """
        schedule.every(minute).minutes.do(job)
        return self

    def hour(self, job: decorator, hour: int = 1) -> 'Timer_Interval':
        """ 间隔多少小时执行一次 """
        schedule.every(hour).hours.do(job)
        return self

    def day(self, job: decorator, day: int = 1) -> 'Timer_Interval':
        """ 间隔多少天执行一次 """
        schedule.every(day).days.do(job)
        return self

    def week(self, job: decorator, week: int = 1) -> 'Timer_Interval':
        """ 间隔多少周执行一次 """
        schedule.every(week).weeks.do(job)
        return self

    def run(self) -> None:
        """ 运行 """
        print(f'[{self.id}] Timer_Interval is running...')
        while True:
            schedule.run_pending()
            time.sleep(1)


class Timer_Specify:
    """ 指定时间执行类 """

    def __init__(self, timer_name: str = 'Timer_Specify') -> None:
        self.id = timer_name

    def minute(self, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每分钟的第几秒执行一次 """
        schedule.every().minute.at(f':{second}').do(job)
        return self

    def hour(self, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每小时的第几分钟的第几秒执行一次 """
        schedule.every().hour.at(f'{minute}:{second}').do(job)
        return self

    def day(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每天的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().day.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def monday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周一的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().monday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def tuesday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周二的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().tuesday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def wednesday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周三的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().wednesday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def thursday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周四的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().thursday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def friday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周五的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().friday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def saturday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周六的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().saturday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def sunday(self, hour: int, minute: int, second: int, job: decorator) -> 'Timer_Specify':
        """ 指定每周日的第几小时的第几分钟的第几秒执行一次 """
        schedule.every().sunday.at(f'{hour}:{minute}:{second}').do(job)
        return self

    def run(self) -> None:
        """ 运行 """
        print(f'[{self.id}] Timer_Specify is running...')
        while True:
            schedule.run_pending()
            time.sleep(1)
