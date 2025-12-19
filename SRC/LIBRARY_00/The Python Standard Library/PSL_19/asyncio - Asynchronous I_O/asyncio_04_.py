#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pytstart/195
    # 🔥 Понимай asyncio как мидл — без магии и мифов
    #
    # Многие пишут async/await, не понимая, что происходит. В
    # итоге код медленный, дебаг невозможен, а блокировки всё
    # равно есть.
    #
    # Вот как работает asyncio — без магии:
    #
    # 📌 1. Event Loop — это «планировщик», который гоняет
    # корутины. Он сам не создаёт потоки. Он ждёт, когда одна
    # задача «освободит» CPU, и сразу берётся за другую.
    #
    # import asyncio
    #
    # async def main():
    #     print("Start")
    #     await asyncio.sleep(1)
    #     print("End")
    #
    # asyncio.run(main())
    #
    # Здесь await asyncio.sleep(1) — не блокирует поток. Это
    # *yield*, который говорит: "я пока жду, можешь заняться чем-
    # то ещё".
    #
    # 📌 2. Ты не должен использовать time.sleep() в async-коде.
    # Это блокирует весь event loop. Заменяй на await
    # asyncio.sleep().
    #
    # 📌 3. Любая синхронная тяжёлая операция — угроза. Например,
    # чтение файла или SQL-запрос через обычный драйвер.
    #
    # ✔️ Как решить:
    #
    # 👍 Используй aiofiles для файлов.
    # 👍 Используй async-драйверы (asyncpg, aiomysql, httpx и т.д.)
    # 👍 Если нет async-аналога — выноси в ThreadPoolExecutor.
    #
    # from concurrent.futures import ThreadPoolExecutor
    # import asyncio
    #
    # def blocking():
    #     ...
    #
    # async def main():
    #     loop = asyncio.get_running_loop()
    #     await loop.run_in_executor(None, blocking)
    #
    # 📌 4. Не забывай про семафоры, если запускаешь 1000 задач
    # одновременно. async не значит всё сразу.
    #
    # sem = asyncio.Semaphore(100)
    #
    # async def safe_task():
    #     async with sem:
    #         await do_something()
    #
    # 🧠 asyncio — это не про параллельность. Это про эффективное
    # переключение задач, которые  ждут  чего-то: ответа сервера,
    # данных, паузы.
    #
    # 🗣 Применяется в: Web-серверах (FastAPI, aiohttp), парсинге,
    # бэкенде с I/O, высоконагруженных API.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
