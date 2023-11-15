import logging
import argparse

FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logs_task2.log', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'ошибка {e} в функии {func.__name__} при аргументах {args}, {kwargs}')
        return None
    return wrapper 

@log_dec
def hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', metavar='a', type=float)
    parser.add_argument('-b', metavar='b', type=float)
    args = parser.parse_args()
    print(f'у катетов {args.a} и {args.b} гипотенуза равна {hypotenuse(args.a, args.b)}')


# Вызов $ python HW\HW15\task2.py -a 6 -b 9