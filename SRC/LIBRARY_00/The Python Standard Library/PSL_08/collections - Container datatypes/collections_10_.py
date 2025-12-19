#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')
    # https://t.me/recura_tech/1745
    # 📱 Использование Python для быстрого анализа логов с помощью
    # collections.Counter.
    #
    # ℹ️ Когда речь заходит об анализе логов на серверах, Python
    # может стать отличным инструментом для быстрой обработки
    # больших файлов и выявления ключевой информации. Один из
    # полезных приемов — использование библиотеки collections, а
    # именно класса Counter, для выявления самых частых строк или
    # паттернов в логах.
    #
    # 📂 Пример:
    #
    # Предположим, у вас есть лог-файл с HTTP-запросами, и вам
    # нужно быстро определить, какие URL запрашивались чаще всего:
    #
    # from collections import Counter
    #
    # # Открываем файл логов
    # with open('access.log') as f:
    #     # Считываем все строки
    #     lines = f.readlines()
    #
    # # Извлекаем только запросы (например, URL после GET)
    # requests = [line.split()[6] for line in lines if 'GET' in
    # line]
    #
    # # Используем Counter для подсчета
    # counter = Counter(requests)
    #
    # # Выводим 10 самых популярных запросов
    # for url, count in counter.most_common(10):
    #     print(f'{url}: {count} запросов')
    #
    # ✳️ Этот подход позволяет вам быстро выявить аномалии или
    # самые популярные ресурсы в логах с минимальными усилиями,
    # что особенно полезно для анализа и мониторинга
    # производительности приложений.
    #
    # from collections import Counter
    #
    # # OTKpbiBaem dain noroB
    #
    # with open('access.log') as f:
    # # CuntbipBaem BCe CTpPOKU
    # lines = f.readlines( )
    #
    # # Vi3enekaemM TOsbKO 3anpocbl (Hanpumep, URL nocne GET)
    # requests = [line.split()[6] for line in lines if 'GET' in line]
    #
    # # Vicnonb3yem Counter ana nogcyueta
    # counter = Counter( requests )
    #
    # # BeiBonum 10 cambix nonynapHbix 3anpocoB
    # for url, count in counter.most_common(10):
    # print(f'{url}: {count} 3anpocos' )

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
