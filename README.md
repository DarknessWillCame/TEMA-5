# Тема 5.Базовые коллекции: множества, списки
Отчет по Теме #5 выполнил(а):

- Черезов Роман Алексеевич
ЗПИЭ-20-1

| Задание   | Сам_раб |
|-----------|---------|
| Задание 1 | +       |
| Задание 2 | +       |
| Задание 3 | +       |
| Задание 4 | +       |
| Задание 5 | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.
## Самостоятельная работа №1
### Ресторан на предприятии ведет учет посещений за неделю при помощи кода работника. У них есть список со всеми посещениями за неделю.
```python
receipts = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

print('Выдано чеков:', len(receipts))

unique_recepts = [];
for x in receipts:
    if x not in unique_recepts:
        unique_recepts.append(x)
print('Количество разных людей посетивших ресторан:', len(unique_recepts))

biggest_count_visit = tuple([-1, 0])
for x in receipts:
    savedCode, savedCount = biggest_count_visit
    count = receipts.count(x)
    if count > savedCount:
        biggest_count_visit = tuple([x, count])
print('Больше всех посетил работник:', biggest_count_visit[0])
```python
## Результат.
![Tema5_1](https://github.com/DarknessWillCame/TEMA-5/assets/46960566/938a164c-c121-4492-81a9-70bbd1c850d1)

Результат задания 1

## Выводы
Для того, чтобы посчитать количество всех чеков можно воспользоваться функцией len()
Для того, чтобы посчитать разных людей можно завести уникальный список и добавлять туда код сотрудника если его ещё нет. После этого можно снова воспользоваться функцией len()
Для того, чтобы найти сотрудника, который посетил ресторан больше всего раз, то необходимо посчитать сколько раз каждый сотрудник был на работе и сравнивать результат с ранее сохранённым и если он больше, то перезаписывать значение
## Самостоятельная работа №2
### На физкультуре студенты сдавали бег, у преподавателя физкультуры есть список всех результатов, ему нужно узнать
```python
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

best_results = []
for x in range(3):
    best_result = min(results)
    best_results.append(best_result)
    results.remove(best_result)
print('Три лучших результата:', best_results)

worst_results = []
for x in range(3):
    worst_result = max(results)
    worst_results.append(worst_result)
    results.remove(worst_result)
print('Три худших результата:', worst_results)

more_than_or_equal_10 = []
for x in results:
    if x >= 10: more_than_or_equal_10.append(x)
print('Все результаты начиная с 10:', more_than_or_equal_10)
```
## Результат.
![Tema5_2](https://github.com/DarknessWillCame/TEMA-5/assets/46960566/bbfa745c-cd28-4259-9305-58ed47d46b31)

Результат задания 2

## Выводы
Чтобы найти три лучших результата необходимо воспользоваться функцией min(). Ищем первый результат, записываем его в отдельный список и удаляем найденное значение из списка в котором ищем. Проделываем это ещё два раза
Чтобы найти три худших результата необходимо воспользоваться функцией max(). Ищем первый результат, записываем его в отдельный список и удаляем найденное значение из списка в котором ищем. Проделываем это ещё два раза
Чтобы найти все результаты начиная с 10, то достаточно пробежаться по списку и при помощи сравнения выписать результаты >10
## Самостоятельная работа №3
### Преподаватель по математике придумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков. Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут указаны два этих значения.
```python
from math import sqrt

def calc_truangle_square_gerone_calc(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print(
    'Площадь из минимальных сторон треугольника:',
    calc_truangle_square_gerone_calc(min(one), min(two), min(three))
)
print(
    'Площадь из максимальных сторон треугольника:',
    calc_truangle_square_gerone_calc(max(one), max(two), max(three))
)
```
## Результат.
![Tema5_3](https://github.com/DarknessWillCame/TEMA-5/assets/46960566/291bf166-ccec-4f9c-8961-9014925a7267)

Результат задания 3

## Выводы
Для поиска площади треугольника я воспользовался формулой Герона. А для поиска минимального и максимального значения воспользовался функциями min() и max()

## Самостоятельная работа №4
### Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки.
```python
example_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
example_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
example_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def rewrite_grade(results):
    new_result = []
    for x in results:
        if x == 2: continue
        if x == 3:
            new_result.append(4)
            continue
        new_result.append(x)
    return new_result

print('Список оценок 1:', rewrite_grade(example_1))
print('Список оценок 2:', rewrite_grade(example_2))
print('Список оценок 3:', rewrite_grade(example_3))
```
## Результат.
![Tema5_4](https://github.com/DarknessWillCame/TEMA-5/assets/46960566/8bfca12f-0226-4b59-a698-89ce6a80c78d)

Результат задания 4

## Выводы
Для решения задачи я написал программу, которая проходится по списку и проверяет каждый элемент. Если элемент является 2, то не добавляем его в новый список. Если элемент равен 3, то меняем его на 4 и добавляем в список

## Самостоятельная работа №5
### Вам предоставлены списки натуральных чисел, из них необходимо сформировать множества. При этом следует соблюдать это правило: если какое-либо число повторяется, то преобразовать его в строку по следующему образцу: например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка «44», строка «444».
```python
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def convert_list_to_set(value):
    result = set()

    while len(value) > 0:
        element = value.pop(0)
        element_count = value.count(element)

        result.add(element)
        for i in range(element_count):
            result.add(str(element) * (i + 2))

    return result

print('Список 1:', convert_list_to_set(list_1))
print('Список 2:', convert_list_to_set(list_2))
print('Список 3:', convert_list_to_set(list_3))
```
## Результат.
![Tema5_5](https://github.com/DarknessWillCame/TEMA-5/assets/46960566/75931890-9165-418d-a893-0cf18fbc19cd)

Результат задания 5

## Выводы
Я выяснил, что для перевода списка в множество необходимо проитеррироваться по списку и проделать необходимые действия над каждым из элементов

## Общие выводы по теме
В ходе выполнения задания я узнал, что язык python содержит удобную структуру данных - list. Благодаря этой структуре можно легко манипулировать элементами, которые она содержит
