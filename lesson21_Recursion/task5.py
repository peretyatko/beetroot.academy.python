# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True
#
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")
#     """

l=[]
def sum_of_digits(a)-> int:
    if(a==0):
        return l
    dig = a % 10
    l.append(dig)
    sum_of_digits(a//10)

n = int(input("Enter a number: "))
sum_of_digits(n)
print(sum(l))
