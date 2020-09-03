# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     """
#     Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True
#     >>> is_palindrome('sassas')
#     True
#     >>> is_palindrome('o')
#     True
#     """
#     pass



def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[len(string) - 1]:
        return is_palindrome(string[1:len(string) - 1])
    else:
        return False

print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))