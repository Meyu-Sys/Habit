import csv
import os
import datetime
import tabulate
import sys
from pathlib import Path

FIELDS = ['Habit', 'Days', 'Date', 'Logs']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


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
    with open('habits.csv', 'a+', newline='') as f:
        clear()

        writer = csv.writer(f)
        hname = input('Enter the name of the habit: ')
        freq = input('Enter the number of days in a week you want to repeat this habit: ')
        hdays = []
        hdate = datetime.date.today()
        hlogs = 0

        for _ in range(int(freq)):
            day = input('Enter the day: ')
            if day not in DAYS:
                print('Invalid day. Please try again.')
                create()
            hdays.append(day)

        writer.writerow([hname, hdays, hdate, hlogs])

        print('Habit created successfully!')
    view()


def log():
    clear()

    with open('habits.csv', 'r') as f:
        reader = csv.reader(f)
        todaylog = []
        lines = []

        for row in reader:
            if tod(row[1], datetime.datetime.today()):
                todaylog.append(row)
            lines.append(row)

        print('Here are the habits you need to log today:')
        print(tabulate.tabulate(todaylog, tablefmt='fancy_grid', headers=FIELDS))

        hname = input('Enter the name of the habit you want to log: ')
        for n in range(len(lines)):
            if lines[n][0] == hname:
                lines[n][3] = 1 + int(lines[n][3])
                print('Habit logged successfully!')
                break
            else:
                print('Habit not found. Please try again.')
                log()

    with open('habits.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

    print('press 1 to go back to the main menu or anything else to quit.')
    match input():
        case '1':
            main()
        case _:
            sys.exit()


def view():
    clear()

    with open('habits.csv', 'r') as f:
        reader = csv.reader(f)

        print('Here are your habits:')
        print(tabulate.tabulate(reader, headers=FIELDS, tablefmt='fancy_grid'))

        match input('Press 1 to go back to the main menu or anything else to quit.'):
            case '1':
                main()
            case _:
                sys.exit()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def tod(x, date) -> bool:
    day = date.weekday()
    today = DAYS[day]
    print(today, x)
    if today in x:
        return True
    else:
        return False


if not os.path.exists('habits.csv'):
    h = Path('habits.csv')
    h.touch()
main()
