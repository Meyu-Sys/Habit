import csv
import os
import datetime
import tabulate
import sys

def main():
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
            print('Invalid input. Please try again.')
            main()

def create():
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
    view()


def log():
    ...

def view():
    print('Here are your habits:')
    print(tabulate.tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
    match input('Press 1 to go back to the main menu or anything else to quit.'):
        case '1':
            main()
        case _:
            sys.exit()

fields = ['habit', 'days', 'date', 'logs']
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
f = open('habits.csv', 'a+')
if os.path.exists('habits.csv'):
    reader = csv.DictReader(f)
    writer = csv.DictWriter(f, fieldnames=fields)
    data = list(reader)
else:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    reader = csv.DictReader(f)
    data = list(reader)
main()
