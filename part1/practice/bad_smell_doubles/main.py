# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self, lst=None):
        if lst is None:
            lst = [3, 2, 1, 4, 2, 1]
        self.lst = lst

    def sorted(self, is_reverse=False):
        return sorted(self.lst, reverse=is_reverse)
