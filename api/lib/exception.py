import logging


class ConditionException(Exception):
    def __str__(self):
        logging.error("condition必须含有type和value属性，且为字符串格式")


class ConditionNotName(Exception):
    def __str__(self):
        logging.error("conditon的type不是name")


    if __name__ == '__main__':
        raise ConditionException()
