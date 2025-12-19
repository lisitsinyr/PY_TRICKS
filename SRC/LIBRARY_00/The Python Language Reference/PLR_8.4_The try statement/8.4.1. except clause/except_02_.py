#------------------------------------------
# except_02_ ():
#------------------------------------------
def except_02_ ():
    """except_02_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', except_02_.__name__)
    print ('#-----------------------------')

    # https://t.me/Python_per_month/3395
    # 🚫 Антипаттерн недели: except: без указания типа исключения
    #
    # В Python использование except: без типа перехватывает все
    # ошибки, включая системные (KeyboardInterrupt, SystemExit).
    # Это может затруднить отладку и скрыть критические проблемы.
    #
    # ✔️ Всегда явно указывайте тип исключения.
    #
    # # X linoxaa npaktuKka
    # try:
    # do_something( )
    # except:
    # print("Mpovzowna own6Ka" )
    #
    # # MepexsatuT Bcé, BKnwoyaa Ctrl+C
    #
    # # @ Jywe trax
    # try:
    # do_something( )
    # except ValueError:
    # print("HekoppekTHoe 3HayeHve" )
    # except (TypeError, ZeroDivisionError) as e:
    # print(f"Ownv6ka: {e}")

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    except_02_ ()
#endif

#endmodule
