import random


def _roll_dice():
    i = 0
    while True:
        val = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        i += 1
        print('%3i:' % i, val[0], val[1], val[2], val[3])
        if val[0] == val[1] == val[2] == val[3]:
            return 'Вы выкинули %i/%i/%i/%i с %i-й попытки.' % (val[0], val[1], val[2], val[3], i)
        else:
            pass


print('Кидаем кубик:')
print(_roll_dice())
print('Вот такие дела.')
print('(это когда хотят сказать "ну как-то так")')
