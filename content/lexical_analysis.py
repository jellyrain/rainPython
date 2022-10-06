from fuzzywuzzy import fuzz, process


class Lexical_Analysis:
    def __init__(self, string: str) -> None:
        self.__lexical = string

    def partial_ratio(self, string: str, weight: float = 0.7) -> bool:
        """ 和字符串 非完全匹配 """
        return (fuzz.partial_ratio(self.__lexical, string) / 100) >= weight

    def token_sort_ratio(self, string: str, weight: float = 0.7) -> bool:
        """ 和字符串 忽略顺序匹配 """
        return (fuzz.token_sort_ratio(self.__lexical, string) / 100) >= weight

    def token_set_ratio(self, string: str, weight: float = 0.7) -> bool:
        """ 和字符串 去重子集匹配 """
        return (fuzz.token_set_ratio(self.__lexical, string) / 100) >= weight

    def list_extract(self, str_list: list[str], weight: float = 0.7) -> list[tuple[str, float]]:
        """ 和列表中字符串匹配 返回 满足权重的值列表 """
        return [(item[0], (item[1] / 100)) for item in process.extract(self.__lexical, str_list) if
                (item[1] / 100) >= weight]

    def list_extractOne(self, str_list: list[str], weight: float = 0.7) -> str | None:
        """ 和列表中字符串匹配 返回满足权重且最匹配的值 没有返回None"""
        return process.extractOne(self.__lexical, str_list)[0] if process.extractOne(self.__lexical, str_list)[
                                                                      1] / 100 >= weight else None


__all__ = ['Lexical_Analysis']
