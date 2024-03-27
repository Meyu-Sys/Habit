import csv
import os
import datetime
import tabulate
import sys
from pathlib import Path

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
    writer = csv.writer(f, fieldnames=fields)
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
    writer.writerow([hname, hdays, hdate, hlogs])
    print('Habit created successfully!')
    f.close()
    view()


def log():
    clear()
    f = open('habits.csv', 'a', newline='')
    reader = csv.reader(f)
    todaylog = filter(reader, tod(reader[1]))
    print('Here are the habits you need to log today:')
    print(tabulate.tabulate(todaylog, tablefmt='fancy_grid', headers='none'))
    hname = input('Enter the name of the habit you want to log: ')
    for row in reader:
        if row[0] == hname:
            row[3] += 1
            print('Habit logged successfully!')
            break
    f.close()
    print('press 1 to go back to the main menu or anything else to quit.')
    match input():
        case '1':
            main()
        case _:
            sys.exit()

def view():
    f = open('habits.csv', 'r')
    reader = csv.reader(f)
    clear()
    print('Here are your habits:')
    print(tabulate.tabulate(reader, headers='firstrow', tablefmt='fancy_grid'))
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

def tod(x) -> bool:
    todayday = datetime.datetime.today().weekday()
    match todayday:
        case 0:
            today = 'Monday'
        case 1:
            today = 'Tuesday'
        case 2:
            today = 'Wednesday'
        case 3:
            today = 'Thursday'
        case 4:
            today = 'Friday'
        case 5:
            today = 'Saturday'
        case 6:
            today = 'Sunday'
    if today in x:
        return True
    else:
        return False

fields = ['Habit', 'Days', 'Date', 'Logs']
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if not os.path.exists('habits.csv'):
    h = Path('habits.csv')
    h.touch()
    f = open('habits.csv', 'a', newline='')
    writer = csv.writer(f,)
    writer.writerow(fields)
    f.close()
main()


## TODO: Add log() function]
## TODO: Fix view() function
    ## TODO: Calculate amount of days habit should have been done until today