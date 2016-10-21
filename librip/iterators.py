# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = 0
        self.items = iter(items) if isinstance(items, list) else items
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.lst=[]
        pass

    def __next__(self):
        while True:
            el = next(self.items)
            if self.ignore_case:
                if el.lower().strip() not in self.lst:
                    self.lst.append(el.lower().strip())
                    return el
            elif el not in self.lst:
                    self.lst.append(el)
                    return el
        raise StopIteration

    def __iter__(self):

        return self
