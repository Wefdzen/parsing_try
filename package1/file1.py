import random

__all__ = ['game']

for_check_f_all = 'hello bro :3'

flag = True

def game():
    """ Game """
    global flag

    print('Welcome in mini game')
    print('You have 100 attempt')
    while flag:
        for i in range(1, 100):
            answer_on_game = random.randint(1, 11)
        answer = int(input('input your num from 1 to 10: '))
        if answer == answer_on_game:
            print('Good job!!!')
            flag = False
        else:
            print('failure  (')
            print(f'The answer was {answer_on_game} \n' )
