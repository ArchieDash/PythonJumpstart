import random


def comparison(answer: int, num: int) -> str:
    if answer > num:
        return 'HIGHER'
    elif answer < num:
        return 'LOWER'


def main():
    num = random.randint(0,100)
    while True:
        answer = int(input('Guess a number between 0 and 100: '))
        if answer != num:
            print(f'Sorry {answer} is {comparison(answer,num)} than the number')
        else:
            print(f'YES! You got it. The number was {num}')
            break


if __name__ == '__main__':
    main()
