"""Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file

```
class CustomException(Exception):
def __init__(self, msg):"""

class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg

a = input('Enter a positive number')

try:
    a = int(a)
    if a < 0:
        raise CustomException('You give negative!')
except ValueError:
    print('it is not a num')
except CustomException as msg:
    with open('msg.txt', 'w', encoding='utf-8') as f:
        f.write(msg)
else:
    print(a)


