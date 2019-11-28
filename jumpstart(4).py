import os
from journal import Journal
import time


def header():
    print('> Welcome to your LOG journal <\n')


def event_loop(journal):
    while True:
        cmd = input('- [L]ist entries\n- [A]dd entry\n- [S]ave journal\n- [U]pload journal\n- e[X]it\n').upper().strip()
        if cmd == 'L':
            journal.log()
        elif cmd == 'A':
            journal.add_entry(input('>>'))
        elif cmd == 'S':
            journal.save()
            print('Journal saved')
        elif cmd == 'U':
            journal.load()
        elif cmd == 'X':
            journal.save()
            print('Goodbye')
            break
        else:
            print(f'{cmd} is undefined command')

            
def main():
    header()
    journal = Journal()
    event_loop(journal)

    
if __name__ == '__main__':
    main()
