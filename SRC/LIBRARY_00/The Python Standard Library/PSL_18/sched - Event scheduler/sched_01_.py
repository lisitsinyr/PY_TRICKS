#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # 10. sched
    #
    # There is increasing interest in the creation of bots and other monitoring and automation applications. For these applications, a common requirement is to perform actions at specified times or
    # specified intervals. This functionality is provided by the sched module in the standard library. There are already similar tools provided
    # by operating systems, such as cron on Linux and Windows Task
    # Scheduler, but with Python’s own sched module you can ignore
    # these platform differences, as well as incorporate scheduled tasks
    # into a program that might have many other functions.
    #
    # import sched
    # import time
    # from datetime import datetime, timedelta
    # scheduler = sched.scheduler(timefunc=time.time)
    # def saytime():
    #   print(time.ctime())
    #   scheduler.enter(10, priority=0, action=saytime)
    # saytime()
    # try:
    #   scheduler.run(blocking=True)
    # except KeyboardInterrupt:
    #   print('Stopped.')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
