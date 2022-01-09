"""
Проба работы с Redis (кэш)
"""

import redis

from pars import span


red = redis.Redis(
    host='redis-18814.c277.us-east-1-3.ec2.cloud.redislabs.com',
    port=18814,
    password='hWx7kuZvPCY1fpQc57rgxspFAe3100zD',
    charset="utf-8"
)

if __name__ == '__main__':
    sp = ''
    for i in span:
        sp = sp + i.getText()+ '\n'
        red.set('span', sp)  # записываем в кэш строку "value1"
    print(red.get('span'))  # считываем из кэша
    #русские буквы не читает!!!!
