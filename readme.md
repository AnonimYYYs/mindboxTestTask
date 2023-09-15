# Тестовое задание

### Как установить библиотеку

Для установки библиотеки в качестве пип-пакета, необходимо использовать
команду: `pip install git+https://{login}:{token}@github.com/AnonimYYYs/mindboxTestTask.git`,
подставив соответствующие значения:

  - login: ваш логин на GitHub 
  - token: как создать токен - [тут](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)


### Использование

*Задание 1:*

``` python
from tasks.task1 import squareCounter

squareCounter.countSquare(3, 4, 5)
>>> 6.0

squareCounter.countSquare(1, 2, 3)
>>> ValueError: Треугольник с такими сторонами не существует.

squareCounter.countSquare(5.0)
>>> 78.53981633974483

squareCounter.countSquare(1, 2, 3, 4, 5, 6)
>>> ValueError: Нет фигуры с заданным количеством параметров
```

*Задание 2:*

Внутри .ipynb файла (src/tasks/task2/pysparkProducts.ipynb)