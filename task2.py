# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application,
# else raise an error. After the user exits, all data should be saved to loaded JSON.



import json
import sys
import os.path


def print_book(book):
    print(json.dumps(book, indent=2, sort_keys=True))


def openbook(book):
    with open(book) as f:
        b = json.load(f)
    return


def get_ss():
    _ = False
    while not _:
        _ = input("Key:\n")
    return _


def find_rec(book):
    action = input("search by:\n"\
        "[f]irst name\n"\
        "[l]ast name\n"\
        "f[u]ll name\n"\
        "[n]umber\n"\
        "[c]ity\n")
    if action == 'n':
        n = get_ss()
        _ = [x for x in book['book'].keys() if x == n]
        if not _:
            print(not found)
        print(book['book'][n])
    else:
        return

def savebook(book):
    print(book)
    with open(book['name'], 'w') as f:
        json.dump(book, f, ensure_ascii=False)


def add_record(book):
    number = input('Number?\n')
    first_name = input('First name?\n'),
    last_name = input('Last name?\n'),
    city = input('city?\n')
    print(last_name)
    book['book'][number] = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': first_name[0] + " " + last_name[0],
        'city': city
    }
    savebook(book)


def delete(book):
    num = input('Number to remove?\n')
    if num in book['book']:
        del book['book'][num]
    else:
        print("No such number")

def update():
    num = input('Number to update?\n')
    if num in book['book']:
        book.update({'number': num})
    else:
        print("No such number")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Where is my phonebook?")
        exit()
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1]) as f:
            book = json.load(f)
    else:
        book = {'name':sys.argv[1], 'book': {}}
    while True:
        action = input('What do you want to do?\n[a]dd, [d]elete, [f]ind, [s]ave, [p]rint, [u]pdate, [q]uit?\n')
        if action == 'a':
            add_record(book)
        elif action == 'd':
            delete(book)
        elif action == 'p':
            print_book(book)
        elif action == 's':
            savebook(book)
        elif action == 'f':
            find_rec(book)
        elif action == 'u':
            update()
        elif action == 'q':
            savebook(book)
            break
        else:
            print('Wrong input')