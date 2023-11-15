# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров. 
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" 
# "Зачет" ставится, если Слушатель успешно выполнил задание. 
# "Незачет" ставится, если Слушатель не выполнил задание. 
# Критерии оценивания: 1 - Слушатель написал корректный код для задачи, 
# добавил к ним логирование ошибок и полезной информации.
import logging
import argparse



FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logs_task1.log', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


class Rectangle:
    def __init__(self, width, height=None):
        if width > 0:
            self._width = width
        else:
            logger.error(f'Ширина должна быть положительной, а не {width}') 
            # raise ValueError                  
        
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Высота должна быть положительной, а не {height}')
                # raise ValueError
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            logger.error(f'Ширина должна быть положительной, а не {value}')
            # raise ValueError               
       

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            logger.error(f'Высота должна быть положительной, а не {value}')
            # raise ValueError

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param', metavar='a b', type=float, nargs=2)
    args = parser.parse_args()

    per = Rectangle(*args.param).perimeter()
    ar = Rectangle(*args.param).area()

    print(f'Периметр {per} и площадь {ar}  прямоугольника со сторонами {args.param[0]} {args.param[1]}')
   
# Вызов $ python HW\HW15\task1.py 3 2