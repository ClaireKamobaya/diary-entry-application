"""Diary Entry Application"""

from datetime import date

DIARY_FILE = 'diary.txt'

def add_entry():
    today = str(date.today())
    entry = input('Write your diary entry: ')
    with open(DIARY_FILE, 'a') as f:
        f.write(f'{today}|{entry}\n')
    print('Entry saved!')

def view_entries():
    search_date = input('Enter date to filter (yyyy-mm-dd): ')
    try:
        with open(DIARY_FILE, 'r') as f:
            lines = f.readlines()
        found = False
        for line in lines:
            parts = line.strip().split('|')
            if parts[0] == search_date:
                print(f'{parts[0]}: {parts[1]}')
                found = True
        if not found:
            print('No entries found for that date.')
    except FileNotFoundError:
        print('No diary entries yet!')

def main():
    while True:
        print('\n--- Diary Menu ---')
        print('1. Add Entry')
        print('2. View Entries by Date')
        print('3. Quit')
        choice = input('Choose an option: ')
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter 1, 2, or 3.')

if __name__ == '__main__':
    main()