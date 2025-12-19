#------------------------------------------
# Decorators_08_ ():
#------------------------------------------
def Decorators_08_ ():
    """Decorators_08_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Decorators_08_.__name__)
    print ('#-----------------------------')

    # Python decorators: 5 + 1 useful decorators to adopt immediately
    # Chris Karvouniaris
    # Chris Karvouniaris
    #
    # ·
    # Follow
    #
    # 9 min read
    # ·
    # Jun 10
    #
    #
    #
    # In the vast realm of Python programming, decorator functions stand out as one of the most elegant and powerful features. They offer a concise and flexible way to modify or extend the behavior of functions, methods, or classes without the need for intrusive code modifications. By decorating a function, you can effortlessly enhance its functionality, encapsulate common behaviors, or add additional functionality without cluttering the original codebase.
    #
    # Python decorator functions act as wrappers around the target functions, providing a higher-order function that takes in the original function as an argument and returns a new function that incorporates the desired modifications. This unique ability to modify and enhance functions dynamically makes decorators an invaluable tool in a developer’s arsenal.
    #
    # Decorators enable a wide range of use cases, including logging, timing, caching, access control, validation, and much more. They promote code reuse and maintainability by separating cross-cutting concerns and promoting modular and composable code. The power lies in their ability to modify function behavior transparently, without modifying the existing code, resulting in cleaner, more concise, and highly reusable codebases.
    #
    # Whether you’re a seasoned Pythonista or just starting your journey with the language, understanding and harnessing the potential of decorator functions will undoubtedly elevate your code to new heights of elegance and efficiency.
    #
    # Throughout this article, we will explore we will demonstrate some examples of useful decorators that one can use to bring useful functionality in their functions without messing with the function logic itself.
    #
    # Let’s get started!
    #
    # Retry decorators
    # A lot of times upon writing a function one already knows that this piece of code won’t always run successfully without errors. When that happens, there are times that the programm needs to persist and retry until it finishes this specific task. In those cases we need to retry a specific piece of code like a function. Of course, to be useful and flexible such functionality should be able to be parametrised so that the retry policy can be defined. Usually that means the maximum number of retries and the waiting time before each retry. At this example we will add one more parametrisation which has to do with the types of exceptions that the retry mechanism should take over. For example one could want their piece of code to be retried in case of specific type of exception e.g some ConnectionError but not other types. Such a decorator would look like this:
    #
    # from time import sleep
    # from functools import wraps
    # import logging
    #
    # def retry_upon_exceptions(exceptions, max_retries=3, delay_seconds=1):
    #     def decorator_retry(func):
    #         @wraps(func)
    #         def wrapper_retry(*args, **kwargs):
    #             tries = 0
    #             while tries < max_retries:
    #                 try:
    #                     return func(*args, **kwargs)
    #                 except exceptions as exception:
    #                     logging.warning(f"Function {func.__name__} failed with an "
    #                                     f"exception {exception.__class__.__name__}, "
    #                                     f"retrying in {delay_seconds} seconds")
    #                     tries += 1
    #                     if tries == max_retries:
    #                         raise exception
    #                     sleep(delay_seconds)
    #         return wrapper_retry
    #     return decorator_retry
    # The above piece of code, when used as a decorator wrapping another function will watch out for raised exception during the execution of the wrapped function and if such an exception is raised then it will retry executing the function. Each retry happens after some waiting time of delay and until a maximum number of retries. Those are parameters that can be defined in the decorator calling as well.
    #
    # Example of usage:
    #
    # Firstly let’s define a function that will randomly raises some exceptions:
    #
    # from random import randint
    #
    # def raising_exception_func():
    #     random_num = randint(1, 50)
    #     if random_num % 2 == 0:
    #         raise ValueError("Dummy message on ValueError")
    #     elif random_num % 3 == 0:
    #         raise TypeError("Dummy message on TypeError")
    #     raise KeyError("Dummy message on KeyError")
    # The above function has a pretty simple logic which is to raise three types of exceptions in three different conditions.
    #
    # Now let’s see how we can use our decorator and wrap this function.
    #
    # from random import randint
    #
    # @retry_upon_exceptions(exceptions=(ValueError, TypeError),
    #                        max_retries=10, delay_seconds=1)
    # def raising_exception_func():
    #     random_num = randint(1, 50)
    #     if random_num % 2 == 0:
    #         raise ValueError("Dummy message on ValueError")
    #     elif random_num % 3 == 0:
    #         raise TypeError("Dummy message on TypeError")
    #     raise KeyError("Dummy message on KeyError")
    # So, we have decorated our function to be able to catch exceptions of types ValueError and TypeError and in those cases the function should be retried with an interval delay of 1 second and up to maximum 10 retries.
    #
    # Now let’s see a demontration how that works.
    #
    # Firstly let’s call the function.
    #
    # import logging
    #
    # logging.info("Calling function raising_exception_func")
    # try:
    #     raising_exception_func()
    # except KeyError as exc:
    #     logging.warning(f"Caught exception after retry: {exc}")
    # What we expect to happen is that as the function runs, it may fall into conditions that will trigger the raising exceptions. If that exception is in the set of exceptions that we have defined in our decorator then the function will be retried. Otherwise the function will not be executed again. In that case the function should raise an exception of type KeyError which our code is catching with a try-catch block.
    #
    # Let’s see the result from the execution:
    #
    #
    # INFO:root:Calling function raising_exception_func
    # WARNING:root:Function raising_exception_func failed with an exception ValueError, retrying in 1 seconds
    # WARNING:root:Function raising_exception_func failed with an exception ValueError, retrying in 1 seconds
    # WARNING:root:Function raising_exception_func failed with an exception ValueError, retrying in 1 seconds
    # WARNING:root:Function raising_exception_func failed with an exception TypeError, retrying in 1 seconds
    # WARNING:root:Function raising_exception_func failed with an exception ValueError, retrying in 1 seconds
    # WARNING:root:Caught exception after retry: 'Dummy message on KeyError'
    # So our function has been retried 5 times in a total of 6 executions. The first 5 executions produced an exception in the defined subset of the decorator parameters and that’s why the retry mechanism kicked in. The last execution just raised an exception not caught by the retry decorator and hence the function didn’t execute again, rather than the exception was caught in the outter try-catch block
    #
    # 2. Timing decorators
    #
    # A useful functionality when executing a piece of code is to examine the execution time, so that one can assess the efficiency of an application, meet strict requirements etc. But when one wants to measure some timing, it’s really tedious to run couple of lines of code each time and each place that those are needed. Instead, one can use a decorator function. With this tool, firstly, there is no longer the necessity to repeat the same piece of code here and there, plus, there are no unrelated pieces of code here and there in between one’s application’s code.
    #
    # An example of such a decorator function:
    #
    # from datetime import datetime
    # import logging
    #
    # def timing_decorator(func):
    #     def wrapper(*args, **kwargs):
    #         start_time = datetime.utcnow()
    #         result = func(*args, **kwargs)
    #         end_time = datetime.utcnow()
    #         logging.info(f"Function {func.__name__} took "
    #                      f"{round((end_time - start_time).total_seconds(), 3)} seconds to run.")
    #         return result
    #     return wrapper
    # Example of usage:
    #
    # from time import sleep
    #
    # @timing_decorator
    # def count_function_timing(limit_number, step=1):
    #     counter = 0
    #     while counter < limit_number:
    #         counter += step
    #         sleep(step)
    #     return
    # This function is supposed to execute in a bit more milliseconds added to a the variable limit_number . But how much exactly? Let’s find out!
    #
    # Let’s call our decorated function with an argument for limit_number=3 and step=1 . That should take a bit more than 3 seconds, alright, so let’s see.
    #
    # logging.info("Calling function count_function_timing")
    # count_function_timing(3, step=1)
    # INFO:root:Calling function count_function_timing
    # INFO:root:Function count_function_timing took 3.013 seconds to run.
    # Alright! That took 3.013 seconds to execute!
    #
    # 3. Timing decorators for async coroutines
    #
    # Timing a function is alright for normal asychronous functions. However if one tries to apply the above in an async coroutine then it will sadly not work! For those cases one can enhance the above decorator as this:
    #
    # def async_timing_decorator(func):
    #     async def process(func, *args, **params):
    #         if asyncio.iscoroutinefunction(func):
    #             logging.info("This is a coroutine")
    #             return await func(*args, **params)
    #         else:
    #             logging.info("This is a function")
    #             return func(*args, **params)
    # Example of usage:
    #
    #
    # @async_timing_decorator
    # async def async_count_function_timing(limit_number, step=1):
    #     counter = 0
    #     while counter < limit_number:
    #         counter += step
    #         sleep(step)
    #     return
    #
    # logging.info("Calling coroutine async_count_function_timing")
    # task = async_count_function_timing(3, 1)
    # asyncio.run(task)
    # This results in:
    #
    # INFO:root:Calling coroutine async_count_function_timing
    # INFO:root:This is a coroutine
    # INFO:root:Function async_count_function_timing took 3.016 seconds to run.
    # 4. Caching decorators
    #
    # Caching is a technique used to store frequently accessed data or computation results in a temporary storage space for faster retrieval. The concept behind caching is simple yet powerful: by keeping a copy of data or computation results closer to the application, subsequent requests can be served quickly, without the need to repeat expensive operations or fetch data from slower sources such as databases or external APIs. Caching plays a crucial role in optimizing performance, reducing response times, and improving scalability in various systems, ranging from web applications to machine learning models. By intelligently utilizing caching strategies, developers can achieve significant performance gains and provide a seamless user experience.
    #
    # So, let’s see an example on how to implement a simple custom cache mechanism with a decorator:
    #
    # def custom_cache(func):
    #     cache = {}
    #
    #     def wrapper(*args):
    #         if args in cache:
    #             return cache[args]
    #         else:
    #             result = func(*args)
    #             cache[args] = result
    #             return result
    #     return wrapper
    # What the decorator is essentially doing is storing the outcome of the decorated function in a dictionary. If the function is called again later then the decorator will look first into this dictionary for a cached result. The key in that case above for the dictionary values is the arguments that were provided in the called function. So, when the function gets called again with the same arguments, that means a stored result already exist in our custom dictionary cache. In that case the decorator will not execute the wrapped function at all, rather than will simply return the stored result from the cache.
    #
    # An impressive example to demonstrate the power of cache is a recursive function where code repeats itself and recalculates the partially same outcomes, for example a fibonacci number calculator:
    #
    # Let’s compare how much time it would take to find the 50th fibonacci number when we are using the cache decorator compared to when we don’t:
    #
    # def fibonacci_no_cache(n):
    #     if n <= 1:
    #         return n
    #     else:
    #         return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)
    #
    # @custom_cache
    # def fibonacci_w_cache(n):
    #     if n <= 1:
    #         return n
    #     else:
    #         return fibonacci_w_cache(n-1) + fibonacci_w_cache(n-2)
    # Let’s see how the function performs without a cache to find the 50th fibonacci number (let me grab a ☕️, this will take a while):
    #
    # logging.info(f"Calling function fibonacci_no_cache")
    # fibonacci_first_numbers = 50
    # start = datetime.utcnow()
    # result = fibonacci_no_cache(fibonacci_first_numbers)
    # end = datetime.utcnow()
    # logging.info(f"Calculation without cache for \n"
    #              f"{fibonacci_first_numbers}th fibonacci number took \n"
    #              f"{(end-start).total_seconds()} seconds,\n"
    #              f"result is {result}")
    # INFO:root:Calling function fibonacci_no_cache
    # INFO:root:Calculation without cache for
    # 50th fibonacci number took
    # 1356.809757 seconds,
    # result is 12586269025
    # Ooook , that was looong 😵 ! So it took more than 22 minutes to execute!
    #
    # Now let’s see what happens with just a simple cache decorator added:
    #
    # logging.info(f"Calling function fibonacci_w_cache")
    # start = datetime.utcnow()
    # result = fibonacci_w_cache(fibonacci_first_numbers)
    # end = datetime.utcnow()
    # logging.info(f"Calculation with cache for \n"
    #              f"{fibonacci_first_numbers}th fibonacci number took \n"
    #              f"{(end-start).total_seconds()} seconds, \n"
    #              f"result is {result}")
    # INFO:root:Calling function fibonacci_w_cache
    # INFO:root:Calculation with cache for
    # 50th fibonacci number took
    # 4.7e-05 seconds,
    # result is 12586269025
    # Just, … wow!
    #
    # 5. Logging decorators
    #
    # Logging decorators are incredibly useful tools in Python for enhancing code maintainability, troubleshooting, and gaining valuable insights into the behavior of functions and methods. By applying logging decorators, developers can easily add logging statements to specific functions or classes without cluttering the original codebase. These decorators can automatically log important information such as function inputs, outputs, execution time, and any relevant contextual details.
    #
    # Let’s see an example:
    #
    # def log_execution(func):
    #     @wraps(func)
    #     def wrapper(*args, **kwargs):
    #         logging.info(f"Executing {func.__name__} with positional arguments "
    #                      f"{[arg for arg in args]} and keyword arguments {kwargs}")
    #         result = func(*args, **kwargs)
    #         logging.info(f"Finished executing {func.__name__}")
    #         return result
    #     return wrapper
    # This is a simple decorator to log the execution of a function as well as the arguments that were called with.
    #
    # Let’s see it in action:
    #
    # @log_execution
    # def function_logging(limit_number, step, dummy_kwarg, dummy_kwarg_2):
    #     counter = 0
    #     while counter < limit_number:
    #         counter += step
    #         sleep(counter)
    #     return
    #
    # logging.info("Calling function function_logging")
    # function_logging(4, 1, dummy_kwarg="some string", dummy_kwarg_2=3)
    # This logs out:
    #
    # INFO:root:Calling function function_logging
    # INFO:root:Executing function_logging with positional
    # arguments [4, 1] and keyword
    # arguments {'dummy_kwarg': 'some string', 'dummy_kwarg_2': 3}
    # INFO:root:Finished executing function_logging
    # 6. Send email decorators
    #
    # Some times finding out about a system failure isn’t enough to be just in an application log, but it requires immediate action or awareness. For those types of needs decorators that notify beyond code are useful. A warning email to someone that should be aware of a code failure is ideal. Let’s see how that could be done with a decorator:
    #
    # def email_on_failure(sender_email, password, recipient_email):
    #     def decorator(func):
    #         def wrapper(*args, **kwargs):
    #             try:
    #                 return func(*args, **kwargs)
    #             except Exception as e:
    #                 # format the error message and traceback
    #                 logging.error(f"Exception caught, "
    #                               f"sending an email to {recipient_email} "
    #                               f"via account {sender_email}")
    #                 err_msg = f"Error: {str(e)}\n\nT" \
    #                           f"raceback:\n{traceback.format_exc()}"
    #
    #                 # create the email message
    #                 message = MIMEText(err_msg)
    #                 message['Subject'] = f"{func.__name__} failed"
    #                 message['From'] = sender_email
    #                 message['To'] = recipient_email
    #
    #                 # send the email
    #                 with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #                     smtp.login(sender_email, password)
    #                     smtp.sendmail(sender_email, recipient_email, message.as_string())
    #                 # re-raise the exception
    #                 raise
    #         return wrapper
    #     return decorator
    # Usage:
    #
    # @email_on_failure(sender_email="<sender gmail here>",
    #                   password="<an app password here for sender gmail>",
    #                   recipient_email="recipient gmail here")
    # def critical_function(limit_number, step=1):
    #     counter = 0
    #     while counter < limit_number:
    #         counter += step
    #         sleep(counter)
    #     raise ValueError(f"Exceeded limit {limit_number}")
    # All one have to do is to provide with a sender and recipient email and of course an app password for authentication of the sender, in case of a gmail account.
    #
    # Third party libraries exist out there that automate this process with an account and SDK libraries e.g SendGrid.

#endfunction


#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Decorators_08_ ()
#endif

#endmodule
