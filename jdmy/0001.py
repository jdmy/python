#!/usr/bin/env python

import random


def gen():
    a = ''
    for i in range(1, 9):
        a += str(int(random.uniform(0, 10)))
    a += '\n'
    return a


def clean():
    fp = open("C:/Users/asus/Desktop/aaa.txt", 'w')
    fp.truncate()
    fp.close()


def file_write():
    fp = open("C:/Users/asus/Desktop/aaa.txt", 'a')
    string = gen()
    fp.write(string)
    fp.close()


if __name__ == '__main__':
    clean()
    for i in range(0, 2):
        file_write()
