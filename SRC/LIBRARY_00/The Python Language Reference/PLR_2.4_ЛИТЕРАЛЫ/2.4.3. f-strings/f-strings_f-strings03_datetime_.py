#------------------------------------------
# f_strings_f_strings03_datetime ():
#------------------------------------------
def f_strings_f_strings03_datetime ():
    """f_strings_f_strings03_datetime"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings03_datetime.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    import datetime
    import locale
    # locale.setlocale (
    #     category=locale.LC_ALL,
    #     locale="Russian"  # Note: do not use "de_DE" as it doesn't work
    # )
    locale.setlocale (locale.LC_ALL, 'ru_RU')
    # vartest_datetime: datetime.datetime = datetime.datetime (year=2017, month=1, day=27)
    vartest_datetime: datetime.datetime = datetime.datetime.now (datetime.UTC)
    print ('vartest_datetime default:', vartest_datetime)
    #------------------------------------------
    # %a    Sun     Weekday as locale’s abbreviated name.
    print (f'{vartest_datetime:%a}')
    # %A    Sunday  Weekday as locale’s full name.
    print (f'{vartest_datetime:%A}')
    # %w    0       Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    print (f'{vartest_datetime:%w}')
    #------------------------------------------
    # %d    08      Day of the month as a zero-padded decimal number.
    print (f'{vartest_datetime:%d}')
    # %-d   8       Day of the month as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-d}')
    #------------------------------------------
    # %b    Sep     Month as locale’s abbreviated name.
    print (f'{vartest_datetime:%b}')
    # %B    September   Month as locale’s full name.
    print (f'{vartest_datetime:%B}')
    # %m    09      Month as a zero-padded decimal number.
    print (f'{vartest_datetime:%m}')
    # %-m   9       Month as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-m}')
    #------------------------------------------
    # %y    13      Year without century as a zero-padded decimal number.
    print (f'{vartest_datetime:%y}')
    # %Y    2013    Year with century as a decimal number.
    print (f'{vartest_datetime:%Y}')
    #------------------------------------------
    # %H    07      Hour (24-hour clock) as a zero-padded decimal number.
    print (f'{vartest_datetime:%H}')
    # %-H   7       Hour (24-hour clock) as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-H}')
    #------------------------------------------
    # %I    07      Hour (12-hour clock) as a zero-padded decimal number.
    print (f'{vartest_datetime:%I}')
    # %-I   7       Hour (12-hour clock) as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-I}')
    #------------------------------------------
    # %p    AM      Locale’s equivalent of either AM or PM.
    print (f'{vartest_datetime:%p}')
    #------------------------------------------
    # %M    06      Minute as a zero-padded decimal number.
    print (f'{vartest_datetime:%M}')
    # %-M   6       Minute as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-M}')
    #------------------------------------------
    # %S    05      Second as a zero-padded decimal number.
    print (f'{vartest_datetime:%S}')
    # %-S   5       Second as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-S}')
    #------------------------------------------
    # %f    000000  Microsecond as a decimal number, zero-padded to 6 digits.
    print (f'{vartest_datetime:%f}')
    #------------------------------------------
    # %z    +0000   UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
    print (f'{vartest_datetime:%z}')
    # %Z    UTC     Time zone name (empty string if the object is naive).
    print (f'{vartest_datetime:%Z}')
    #------------------------------------------
    # %j    251     Day of the year as a zero-padded decimal number.
    print (f'{vartest_datetime:%j}')
    # %-j   251     Day of the year as a decimal number. (Platform specific)
    # print (f'{vartest_datetime:%-j}')
    #------------------------------------------
    # %U    36      Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
    print (f'{vartest_datetime:%U}')
    # %-U   36      Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)
    # print (f'{vartest_datetime:%-U}')
    #------------------------------------------
    # %W    35      Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
    print (f'{vartest_datetime:%W}')
    # %-W   35      Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)
    # print (f'{vartest_datetime:%-W}')
    #------------------------------------------
    # %c    Sun Sep 8 07:06:05 2013 Locale’s appropriate date and time representation.
    print (f'{vartest_datetime:%c}')
    #------------------------------------------
    # %x    09/08/13    Locale’s appropriate date representation.
    print (f'{vartest_datetime:%x}')
    # %X    07:06:05    Locale’s appropriate time representation.
    print (f'{vartest_datetime:%X}')
    #------------------------------------------
    # %%    %       A literal '%' character.
    print (f'{vartest_datetime:%%}')

    #------------------------------------------
    #
    #------------------------------------------
    # today = datetime.datetime.utcnow()
    today = datetime.datetime.now(datetime.UTC)
    # print(type(today))
    # print(f'today    : {today}')
    print(f'locale appropriate: {today}')
    # PATTERNS
    print(f'date time: {today:%m/%d/%Y %H:%M:%S}')
    print(f'date     : {today:%m/%d/%Y}')
    print(f'time     : {today:%H:%M:%S.%f}')
    print(f'time     : {today:%H:%M:%S %p}')
    print(f'time     : {today:%H:%M}')
    #------------------------------------------
    # %A weekday
    print(f'weekday: {today:%A}')
    # %c
    print(f'locale appropriate: {today:%c}')
    # day of the year
    print(f'day of year: {today:%j}')
    #------------------------------------------
    # how far are we into the year?
    day_of_year = f'{today:%j}'
    print(f'progress % year: {int(day_of_year)/365 * 100:.2f}%')
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings03_datetime ()
#endif

#endmodule
