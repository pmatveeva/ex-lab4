import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0, 'No args'
    i = 0
    if len(args)==1:
        while i < len(items):
            if items[i].get(args[0]) is not None:
                yield items[i].get(args[0])
            else:
                continue
            i += 1
    else:

        while i < len(items):
            d = {}
            for el in args:
                if items[i].get(el) is not None:
                    d[el] = items[i].get(el)
            if len(d)!=0:
                yield d
            i += 1


    # Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки


def gen_random(begin, end, num_count):
    pass
    for i in range(num_count):
        yield random.randint(begin, end)
