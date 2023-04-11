#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    s = input("Введите предложение: ")
    nns = []
    for i, word in enumerate(s):
        if s[i:i+2] == "нн":
            nns.append(s[i:i+2])
    print("Все буквосочетанния в предложении: {0}".format(nns))
    input("Нажмите на любую кнопку, чтобы выйти!")
