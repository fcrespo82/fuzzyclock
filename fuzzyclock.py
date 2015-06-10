#! /usr/bin/env python
# coding: utf-8

import datetime
import sys

def parseHour(hour):
    hourList = ("uma", "duas", "tres", "quatro", "cinco", "seis",
                "sete", "oito", "nove", "dez", "onze", "meio dia")

    return "meia noite" if hour == 24 else hourList[(hour%12)-1]

def junction(hour):
    junctionList = [
        ([1, 13, 24], " a "),
        ([12], " o "),
    ]
    for theRange, theText in junctionList:
        if hour in theRange:
            return theText

    return " as "

def parseMinute(hour, minute):
    minuteList = [
        (range(3, 8), parseHour(hour) + " e cinco"),
        (range(3, 8), parseHour(hour) + " e cinco"),
        (range(8, 13), parseHour(hour) + " e dez"),
        (range(13, 18), parseHour(hour) + " e quinze"),
        (range(18, 23), parseHour(hour) + " e vinte"),
        (range(23, 28), parseHour(hour) + " e vinte e cinco"),
        (range(28, 33), parseHour(hour) + " e meia"),
        (range(33, 38), parseHour(hour) + " e trinta e cinco"),
        (range(38, 43), "vinte para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(43, 48), "quinze para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(48, 53), "dez para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(53, 58), "cinco para" + junction(hour + 1) + parseHour(hour + 1)),
    ]
    for theRange, theText in minuteList:
        if minute in theRange:
            return theText

    return parseHour(hour)

def main():
    h = int(sys.argv[1]) if len(sys.argv) > 2 else datetime.datetime.now().time().hour
    m = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().time().minute
    print(parseMinute(h, m))

main()

# for i in range(0, 24):
#     print(i, junction(i), parseMinute(i, 40))
