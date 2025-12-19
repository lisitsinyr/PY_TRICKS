#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/pythonl/4833
    #
    # Дата: 2025-05-27 13:02:56+00:00
    #
    # Title: Python/ django
    #
    # 🖥 **Хитрая задача на Python для продвинутых: словарь,
    # который работает как список**
    #
    # Представь структуру данных, которая:
    # • работает как `dict` — доступ по ключу
    # • работает как `list` — доступ по индексу
    # • сохраняет порядок вставки
    # • поддерживает `.index(key)` и `.key_at(i)`
    #
    # 📌 **Задача**: Реализуй класс `IndexedDict`, который делает
    # всё это.
    #
    # **🔍 Пример использования:**
    #
    # ```
    # d = IndexedDict()
    # d["a"] = 10
    # d["b"] = 20
    # d["c"] = 30
    #
    # print(d["a"])        # 10
    # print(d[0])          # 10
    # print(d[1])          # 20
    # print(d.key_at(1))   # "b"
    # print(d.index("c"))  # 2
    #
    # for k in d:
    #     print(k, d[k])   # перебор по ключам
    # ```
    #
    # ⚠️ Подвох:
    #
    # • Просто наследовать `dict` не получится — `d[0]` будет
    # интерпретироваться как ключ, а не индекс
    # • Придётся реализовать двойную логику доступа вручную
    # • Нужно корректно поддержать `__iter__`, `__getitem__`,
    # `__len__` и др.
    #
    # ✅ Решение:
    #
    # ```python
    # from collections.abc import MutableMapping
    #
    # class IndexedDict(MutableMapping):
    #     def __init__(self):
    #         self._data = {}
    #         self._keys = []
    #
    #     def __getitem__(self, key):
    #         if isinstance(key, int):
    #             real_key = self._keys[key]
    #             return self._data[real_key]
    #         return self._data[key]
    #
    #     def __setitem__(self, key, value):
    #         if key not in self._data:
    #             self._keys.append(key)
    #         self._data[key] = value
    #
    #     def __delitem__(self, key):
    #         if key in self._data:
    #             self._keys.remove(key)
    #             del self._data[key]
    #
    #     def __iter__(self):
    #         return iter(self._keys)
    #
    #     def __len__(self):
    #         return len(self._data)
    #
    #     def index(self, key):
    #         return self._keys.index(key)
    #
    #     def key_at(self, idx):
    #         return self._keys[idx]
    # ```
    #
    # 📈 Зачем это нужно:
    #
    # • Отличная тренировка на переопределение магических методов
    # • Часто встречается в фреймворках (Pandas, SQLAlchemy)
    # • Тестирует знание ABC-классов
    # (`collections.abc.MutableMapping`)
    # • Полезно для построения кастомных структур данных

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
