Link: https://t.me/school_network/2189

Дата: 2025-07-16 17:15:20+00:00

Title: Серверная Админа | Компьютерные сети

👋 `Привет, сетевой друг!
`
`Сегодня покажу, как разобрать вывод show-команд в четкий
формат с помощью ``shconfparser`

🟣**Как это работает:**
shconfparser умеет читать текст из show-команд (например,
show run, show version, show ip interface brief) и
превращать всё это в дерево, таблицу или словарь.

🟣Базовый пример:

```from shconfparser.parser import Parser
from os import path

file_path = path.abspath('data/shcommands.txt')
p = Parser()

raw = p.read(file_path)               # читаем файл с show-
командами
data = p.split(raw)                   # делим по типам
(running, version, и т.д.)```

🟣Парсим show run в дерево:

```data['running'] = p.parse_tree(data['running'])
p.dump(data['running'], indent=4)```

🟣Парсим таблицу (например, show cdp neighbors):

```header = ['Device ID', 'Local Intrfce', 'Holdtme',
'Capability', 'Platform', 'Port ID']
data['cdp_neighbors'] = p.parse_table(data['cdp_neighbors'],
header)
p.dump(data['cdp_neighbors'], indent=4)```

🟣Ищем интерфейсы в дереве:

```pattern = r'interface\s+FastEthernet.*'
matches = p.search.search_all_in_tree(pattern,
data['running'])
print(matches.values())```

🟣Или ищем узел в таблице:

```pattern = r'R\d+'
result = p.search.search_in_table(pattern,
data['cdp_neighbors'], header='Device ID')
print(result)```

[**Серверная Админа**](https://t.me/school_network) | #Network

