#! /usr/bin/env python
# coding: utf-8

import datetime
import sys

def switch(x, caseList, default):
    for theRange, theResponse in caseList:
        if x in theRange:
            return theResponse()
    return default

def parseHour(hour):
    hourList = ("uma", "duas", "tres", "quatro", "cinco", "seis",
                "sete", "oito", "nove", "dez", "onze", "meio dia")

    return "meia noite" if hour == 24 else hourList[(hour%12)-1]

def junction(hour):
    junctionList = [
        ([1, 13, 24, 25], lambda:" a "),
        ([12], lambda:" o "),
    ]

    return switch(hour, junctionList, " as ")

def parseTime(hour, minute):
    minuteList = [
        (range(3, 8), lambda:parseHour(hour) + " e cinco"),
        (range(8, 13), lambda:parseHour(hour) + " e dez"),
        (range(13, 18), lambda:parseHour(hour) + " e quinze"),
        (range(18, 23), lambda:parseHour(hour) + " e vinte"),
        (range(23, 28), lambda:parseHour(hour) + " e vinte e cinco"),
        (range(28, 33), lambda:parseHour(hour) + " e meia"),
        (range(33, 38), lambda:parseHour(hour) + " e trinta e cinco"),
        (range(38, 43), lambda:"vinte para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(43, 48), lambda:"quinze para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(48, 53), lambda:"dez para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(53, 58), lambda:"cinco para" + junction(hour + 1) + parseHour(hour + 1)),
        (range(58, 60), lambda:parseHour(hour + 1)),
        (range(0, 3), lambda:parseHour(hour)),
    ]

    return switch(minute, minuteList, parseHour(hour))

def main():
    h = int(sys.argv[1]) if len(sys.argv) > 2 else datetime.datetime.now().time().hour
    m = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().time().minute
    print(parseTime(h, m))

main()
