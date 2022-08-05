import random
import math

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)


def _词转换(x, y, 淫乱度):
#   print(x,y)
    if random.random() > 淫乱度:
        return x
    if x in {'!', '！'}:
        return '❤'
    if y == 'x':
        return ['……嗯……', '……不要……', '……哈啊……', '……呜喵……', '……要…去了……'][math.ceil(淫乱度 * 5) - 1]
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}……{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = '〇' * len(x)
        return f'……{x}'


def chs2yin(s, 淫乱度=0.5):
    if 淫乱度 > 1 or 淫乱度 < 0: 淫乱度 = 0.5
    return ''.join([_词转换(x, y, 淫乱度) for x, y in pseg.cut(s)])


if __name__ == '__main__':
    print(chs2yin('不行，那里不行。'))
