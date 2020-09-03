# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True
#     """
def reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1
print(reverse('hello'))
print(reverse('o'))