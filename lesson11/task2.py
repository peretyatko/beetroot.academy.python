# Task 2
# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists. The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
# ```
# class Mathematician:
#     pass
# m = Mathematician()
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
def square(list):
    return [i ** 2 for i in list]

def remove_positives(list):
    for item in list:
        if item > 0:
            list.remove(item)
    print(list)

def filter_leaps(list):
    newlist = []
    for item in list:
        if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
            newlist.append(item)
    print(newlist)



list1 = [7, 11, 5, 4]
print(square(list1))
list2 = [26, -11, -8, 13, -90]
remove_positives(list2)
list3 = [2001, 1884, 1995, 2003, 2020]

filter_leaps(list3)
