import csv
import os
import datetime
import tabulate
import sys

FIELDS = ['Habit', 'Days', 'Date', 'Logs']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
NAME = 'habits.csv'

def main():
    clear()

    print('Welcome to Habit Tracker!')
    print('What would you like to do?')
    print('1. Create a new habit')
    print('2. Log a habit')
    print('3. View habits')

    choice = input('Enter the number of your choice: ')
    match choice:
        case '1':
            clear()
            create(NAME)
        case '2':
            clear()
            log(NAME)
        case '3':
            clear()
            print('Here are your habits:')
            print(view(NAME))
            coy = input('press 1 to go back to the main menu or anything else to quit.')
            match coy:
                case '1':
                    main()
                case _:
                    sys.exit()

        case _:
            sys.exit()


def create(file=NAME):
    with open(file, 'a+', newline='') as f:

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
                sys.exit()
            else:
                hdays.append(day)

        writer.writerow([hname, hdays, hdate, hlogs])

        print('Habit created successfully!')
    print(view(NAME))


def log(file=NAME):
    with open(file, 'r') as f:
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
                continue

    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)



def view(file=NAME):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        return tabulate.tabulate(reader, headers=FIELDS, tablefmt='fancy_grid')


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


def createcsv(file):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)


if not os.path.exists(NAME):
    createcsv(NAME)

if __name__ == '__main__':
    main()
