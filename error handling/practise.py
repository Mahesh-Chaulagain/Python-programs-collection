# No errors in the 'try' clause
# x = 1
# try:
#     print(5 / x)
# except ZeroDivisionError:
#     print('something went wrong')
# print("i am executing after the try clause")


# Errors in the 'try' clause and the Exception is specified
# x = 0
# try:
#     print(5 / x)
# except ZeroDivisionError:
#     print("something went wrong")
# print("i am executing after the try clause!")



# Errors in the 'try' clause and the exception is not specified
# x = 0
# try: 
#     print(5 / y)
# except ZeroDivisionError:   # exception is NameError
#     print("something went wrong")
# print("i am executing after the try clause")



# code with 'finally' block and 'try' block that doesn't throw error
# x = 1
# try: 
#     print(5 / x)
# except ZeroDivisionError:
#     print("I am the except clause")
# finally:
#     print("i am the finally clause")

# print("i am executing after the try clause")


# if the code in the 'try' clause executes without throwing an error, then the code in the 'else' clause will also execute
# x = 1
# try: 
#     print(5 / x)
# except ZeroDivisionError:
#     print("I am the except clause")
# else:
#     print('i am the else clause')
# finally:
#     print("i am the finally clause")

# print("i am executing after the try clause")


# if we experience an exception or error in the 'try' clause, the 'else' clause would be ignored
# x = 0
# try: 
#     print(5 / x)
# except ZeroDivisionError:
#     print("I am the except clause")
# else:
#     print('i am the else clause')
# finally:
#     print("i am the finally clause")

# print("i am executing after the try clause")


# custom exceptions
class FooError(Exception):  # create a class and extend it from the Exception class
    def __init__(self, message):
        self.message = message

    def foo(self):
        print("bar")

try: 
    raise FooError("this is a test error")
except FooError as e:
    e.foo()

    

