#! /usr/bin/env python
# coding: utf-8

import datetime
import sys

def parseHour(hour):
    hourList = ("meia noite", "uma", "duas", "tres", "quatro", "cinco", "seis",
                "sete", "oito", "nove", "dez", "onze", "meio dia")
    if hour > 23:
        hour = 0
    elif hour > 12:
        hour = hour - 12
    return hourList[hour]

def junction(hour):
    if hour <= 1 or hour == 13 or hour >= 23:
        return "a"
    elif hour == 12:
        return "o"
    else:
        return "as"

def parseMinute(hour, minute):
    if 3 <= minute < 8:
        return parseHour(hour) + " e cinco"
    elif 8 <= minute < 13:
        return parseHour(hour) + " e dez"
    elif 13 <= minute < 18:
        return parseHour(hour) + " e quinze"
    elif 18 <= minute < 23:
        return parseHour(hour) + " e vinte"
    elif 23 <= minute < 28:
        return parseHour(hour) + " e vinte e cinco"
    elif 28 <= minute < 33:
        return parseHour(hour) + " e meia"
    elif 33 <= minute < 38:
        return "vinte e cinco para {0} {1}".format(junction(hour + 1), parseHour(hour + 1))
    elif 38 <= minute < 43:
        return "vinte para {0} {1}".format(junction(hour + 1), parseHour(hour + 1))
    elif 43 <= minute < 48:
        return "quinze para {0} {1}".format(junction(hour + 1), parseHour(hour + 1))
    elif 48 <= minute < 53:
        return "dez para {0} {1}".format(junction(hour + 1), parseHour(hour + 1))
    elif 53 <= minute < 58:
        return "cinco para {0} {1}".format(junction(hour + 1), parseHour(hour + 1))
    else:
        return parseHour(hour)

def main():
    h = int(sys.argv[1]) if len(sys.argv) > 2 else datetime.datetime.now().time().hour
    m = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().time().minute
    print(parseMinute(h, m))

main()
