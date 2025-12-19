#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Code    Example     Description
    # %a      Sun         Weekday as locale’s abbreviated name.
    # %A      Sunday      Weekday as locale’s full name.
    # %w      0           Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    # %d      08          Day of the month as a zero-padded decimal number.
    # %-d     8           Day of the month as a decimal number. (Platform specific)
    # %b      Sep         Month as locale’s abbreviated name.
    # %B      September   Month as locale’s full name.
    # %m      09          Month as a zero-padded decimal number.
    # %-m     9           Month as a decimal number. (Platform specific)
    # %y      13          Year without century as a zero-padded decimal number.
    # %Y      2013        Year with century as a decimal number.
    # %H      07          Hour (24-hour clock) as a zero-padded decimal number.
    # %-H     7           Hour (24-hour clock) as a decimal number. (Platform specific)
    # %I      07          Hour (12-hour clock) as a zero-padded decimal number.
    # %-I     7           Hour (12-hour clock) as a decimal number. (Platform specific)
    # %p      AM          Locale’s equivalent of either AM or PM.
    # %M      06          Minute as a zero-padded decimal number.
    # %-M     6           Minute as a decimal number. (Platform specific)
    # %S      05          Second as a zero-padded decimal number.
    # %-S     5           Second as a decimal number. (Platform specific)
    # %f      000000      Microsecond as a decimal number, zero-padded to 6 digits.
    # %z      +0000       UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
    # %Z      UTC         Time zone name (empty string if the object is naive).
    # %j      251         Day of the year as a zero-padded decimal number.
    # %-j     251         Day of the year as a decimal number. (Platform specific)
    # %U      36          Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
    # %-U     36          Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)
    # %W      35          Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
    # %-W     35          Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)
    # %c      Sun Sep 8 07:06:05 2013
    #                     Locale’s appropriate date and time representation.
    # %x      09/08/13    Locale’s appropriate date representation.
    # %X      07:06:05    Locale’s appropriate time representation.
    # %%      %           A literal '%' character.
    #
    #
    # [//]: # (strftime - format date and time)
    #
    # %a     The abbreviated name of the day of the week according to
    #       the current locale.  (Calculated from tm_wday.)  (The
    #       specific names used in the current locale can be obtained
    #       by calling nl_langinfo(3) with ABDAY_{1–7} as an argument.)
    #
    # %A     The full name of the day of the week according to the
    #       current locale.  (Calculated from tm_wday.)  (The specific
    #       names used in the current locale can be obtained by calling
    #       nl_langinfo(3) with DAY_{1–7} as an argument.)
    #
    # %b     The abbreviated month name according to the current locale.
    #       (Calculated from tm_mon.)  (The specific names used in the
    #       current locale can be obtained by calling nl_langinfo(3)
    #       with ABMON_{1–12} as an argument.)
    #
    # %B     The full month name according to the current locale.
    #       (Calculated from tm_mon.)  (The specific names used in the
    #       current locale can be obtained by calling nl_langinfo(3)
    #       with MON_{1–12} as an argument.)
    #
    # %c     The preferred date and time representation for the current
    #       locale.  (The specific format used in the current locale
    #       can be obtained by calling nl_langinfo(3) with D_T_FMT as
    #       an argument for the %c conversion specification, and with
    #       ERA_D_T_FMT for the %Ec conversion specification.)  (In the
    #       POSIX locale this is equivalent to %a %b %e %H:%M:%S %Y.)
    #
    # %C     The century number (year/100) as a 2-digit integer. (SU)
    #       (The %EC conversion specification corresponds to the name
    #       of the era.)  (Calculated from tm_year.)
    #
    # %d     The day of the month as a decimal number (range 01 to 31).
    #       (Calculated from tm_mday.)
    #
    # %D     Equivalent to %m/%d/%y.  (Yecch—for Americans only.
    #       Americans should note that in other countries %d/%m/%y is
    #       rather common.  This means that in international context
    #       this format is ambiguous and should not be used.) (SU)
    #
    # %e     Like %d, the day of the month as a decimal number, but a
    #       leading zero is replaced by a space. (SU) (Calculated from
    #       tm_mday.)
    #
    # %E     Modifier: use alternative ("era-based") format, see below.
    #       (SU)
    #
    # %F     Equivalent to %Y-%m-%d (the ISO 8601 date format). (C99)
    #
    # %G     The ISO 8601 week-based year (see NOTES) with century as a
    #       decimal number.  The 4-digit year corresponding to the ISO
    #       week number (see %V).  This has the same format and value
    #       as %Y, except that if the ISO week number belongs to the
    #       previous or next year, that year is used instead. (TZ)
    #       (Calculated from tm_year, tm_yday, and tm_wday.)
    #
    # %g     Like %G, but without century, that is, with a 2-digit year
    #       (00–99). (TZ) (Calculated from tm_year, tm_yday, and
    #       tm_wday.)
    #
    # %h     Equivalent to %b.  (SU)
    #
    # %H     The hour as a decimal number using a 24-hour clock (range
    #       00 to 23).  (Calculated from tm_hour.)
    #
    # %I     The hour as a decimal number using a 12-hour clock (range
    #       01 to 12).  (Calculated from tm_hour.)
    #
    # %j     The day of the year as a decimal number (range 001 to 366).
    #       (Calculated from tm_yday.)
    #
    # %k     The hour (24-hour clock) as a decimal number (range 0 to
    #       23); single digits are preceded by a blank.  (See also %H.)
    #       (Calculated from tm_hour.)  (TZ)
    #
    # %l     The hour (12-hour clock) as a decimal number (range 1 to
    #       12); single digits are preceded by a blank.  (See also %I.)
    #       (Calculated from tm_hour.)  (TZ)
    #
    # %m     The month as a decimal number (range 01 to 12).
    #       (Calculated from tm_mon.)
    #
    # %M     The minute as a decimal number (range 00 to 59).
    #       (Calculated from tm_min.)
    #
    # %n     A newline character. (SU)
    #
    # %O     Modifier: use alternative numeric symbols, see below. (SU)
    #
    # %p     Either "AM" or "PM" according to the given time value, or
    #       the corresponding strings for the current locale.  Noon is
    #       treated as "PM" and midnight as "AM".  (Calculated from
    #       tm_hour.)  (The specific string representations used for
    #       "AM" and "PM" in the current locale can be obtained by
    #       calling nl_langinfo(3) with AM_STR and PM_STR,
    #       respectively.)
    #
    # %P     Like %p but in lowercase: "am" or "pm" or a corresponding
    #       string for the current locale.  (Calculated from tm_hour.)
    #       (GNU)
    #
    # %r     The time in a.m. or p.m. notation.  (SU) (The specific
    #       format used in the current locale can be obtained by
    #       calling nl_langinfo(3) with T_FMT_AMPM as an argument.)
    #       (In the POSIX locale this is equivalent to %I:%M:%S %p.)
    #
    # %R     The time in 24-hour notation (%H:%M).  (SU) For a version
    #       including the seconds, see %T below.
    #
    # %s     The number of seconds since the Epoch, 1970-01-01 00:00:00
    #       +0000 (UTC). (TZ) (Calculated from mktime(tm).)
    #
    # %S     The second as a decimal number (range 00 to 60).  (The
    #       range is up to 60 to allow for occasional leap seconds.)
    #       (Calculated from tm_sec.)
    #
    # %t     A tab character. (SU)
    #
    # %T     The time in 24-hour notation (%H:%M:%S).  (SU)
    #
    # %u     The day of the week as a decimal, range 1 to 7, Monday
    #       being 1.  See also %w.  (Calculated from tm_wday.)  (SU)
    #
    # %U     The week number of the current year as a decimal number,
    #       range 00 to 53, starting with the first Sunday as the first
    #       day of week 01.  See also %V and %W.  (Calculated from
    #       tm_yday and tm_wday.)
    #
    # %V     The ISO 8601 week number (see NOTES) of the current year as
    #       a decimal number, range 01 to 53, where week 1 is the first
    #       week that has at least 4 days in the new year.  See also %U
    #       and %W.  (Calculated from tm_year, tm_yday, and tm_wday.)
    #       (SU)
    #
    # %w     The day of the week as a decimal, range 0 to 6, Sunday
    #       being 0.  See also %u.  (Calculated from tm_wday.)
    #
    # %W     The week number of the current year as a decimal number,
    #       range 00 to 53, starting with the first Monday as the first
    #       day of week 01.  (Calculated from tm_yday and tm_wday.)
    #
    # %x     The preferred date representation for the current locale
    #       without the time.  (The specific format used in the current
    #       locale can be obtained by calling nl_langinfo(3) with D_FMT
    #       as an argument for the %x conversion specification, and
    #       with ERA_D_FMT for the %Ex conversion specification.)  (In
    #       the POSIX locale this is equivalent to %m/%d/%y.)
    #
    # %X     The preferred time representation for the current locale
    #       without the date.  (The specific format used in the current
    #       locale can be obtained by calling nl_langinfo(3) with T_FMT
    #       as an argument for the %X conversion specification, and
    #       with ERA_T_FMT for the %EX conversion specification.)  (In
    #       the POSIX locale this is equivalent to %H:%M:%S.)
    #
    # %y     The year as a decimal number without a century (range 00 to
    #       99).  (The %Ey conversion specification corresponds to the
    #       year since the beginning of the era denoted by the %EC
    #       conversion specification.)  (Calculated from tm_year)
    #
    # %Y     The year as a decimal number including the century.  (The
    #       %EY conversion specification corresponds to the full
    #       alternative year representation.)  (Calculated from
    #       tm_year)
    #
    # %z     The +hhmm or -hhmm numeric timezone (that is, the hour and
    #       minute offset from UTC). (SU)
    #
    # %Z     The timezone name or abbreviation.
    #
    # %+     The date and time in date(1) format. (TZ) (Not supported in
    #       glibc2.)
    #
    # %%     A literal '%' character.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
