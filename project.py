import csv
import os
import datetime
import tabulate
import sys

def main():
    clear()
    print('Welcome to Habit Tracker!')
    print('What would you like to do?')
    print('1. Create a new habit')
    print('2. Log a habit')
    print('3. View habits')
    match input('Enter the number of your choice: '):
        case '1':
            create()
        case '2':
            log()
        case '3':
            view()
        case _:
            f.close()
            sys.exit()

def create():
    f = open('habits.csv', 'a', newline='')
    writer = csv.DictWriter(f, fieldnames=fields)
    clear()
    hname = input('Enter the name of the habit: ')
    freq = input('Enter the number of days in a week you want to repeat this habit: ')
    hdays = []
    for _ in range(int(freq)):
        day = input('Enter the day: ')
        if day not in Days:
            print('Invalid day. Please try again.')
            create()
        hdays.append(day)
    hdate = datetime.date.today()
    hlogs = 0
    writer.writerow({'habit': hname, 'days': hdays, 'date': hdate, 'logs': hlogs})
    print('Habit created successfully!')
    f.close()
    view()


def log():
    ...

def view():
    f = open('habits.csv', 'r')
    reader = csv.DictReader(f)
    clear()
    print('Here are your habits:')
    print(tabulate.tabulate(list(reader), headers='firstrow', tablefmt='fancy_grid'))
    match input('Press 1 to go back to the main menu or anything else to quit.'):
        case '1':
            f.close()
            main()
        case _:
            f.close()
            sys.exit()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

fields = ['habit', 'days', 'date', 'logs']
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if not os.path.exists('habits.csv'):
    if os.name == 'nt':
        f = open('./habits.csv', 'a', newline='')
    else:
        os.mknod('./habits.csv')
        f = open('./habits.csv', 'a')
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    f.close()
main()

## TODO: Add log() function]
## TODO: Fix view() function
    ## Maybe open and close file evry time a new operation is done alongside reader and writer
    ## TODO: Calculate amount of days habit should have been done until today