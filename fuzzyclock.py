#! /usr/bin/env python
# coding: utf-8

import datetime
import sys

def parseHour(hour):
    if hour in [1, 13]:
        return "uma"
    elif hour in [2, 14]:
        return "duas"
    elif hour in [3, 15]:
        return "três"
    elif hour in [4, 16]:
        return "quatro"
    elif hour in [5, 17]:
        return "cinco"
    elif hour in [6, 18]:
        return "seis"
    elif hour in [7, 19]:
        return "sete"
    elif hour in [8, 20]:
        return "oito"
    elif hour in [9, 21]:
        return "nove"
    elif hour in [10, 22]:
        return "dez"
    elif hour in [11, 23]:
        return "onze"
    elif hour in [0,24]:
        return "meia noite"
    elif hour in [12]:
        return "meio dia"

def parseMinute(hour, minute):
    if minute >= 57 or minute < 3:
        return parseHour(hour)
    elif minute >= 3 and minute < 7:
        return parseHour(hour) + " e cinco"
    elif minute >= 7 and minute < 13:
        return parseHour(hour) + " e dez"
    elif minute >= 13 and minute < 17:
        return parseHour(hour) + " e quinze"
    elif minute >= 17 and minute < 23:
        return parseHour(hour) + " e vinte"
    elif minute >= 23 and minute < 27:
        return parseHour(hour) + " e vinte e cinco"
    elif minute >= 27 and minute < 33:
        return parseHour(hour) + " e meia"
    elif minute >= 33 and minute < 37:
        return "vinte e cinco para {0}{1}".format("as " if hour < 23 else "a ", parseHour(hour + 1))
    elif minute >= 37 and minute < 43:
        return "vinte para {0}{1}".format("as " if hour < 23 else "a ", parseHour(hour + 1))
    elif minute >= 43 and minute < 47:
        return "quinze para {0}{1}".format("as " if hour < 23 else "a ", parseHour(hour + 1))
    elif minute >= 47 and minute < 53:
        return "dez para {0}{1}".format("as " if hour < 23 else "a ", parseHour(hour + 1))
    elif minute >= 53 and minute < 57:
        return "cinco para {0}{1}".format("as " if hour < 23 else "a ", parseHour(hour + 1))

def parseDate():
    h=int(sys.argv[1]) if len(sys.argv) > 2 else datetime.datetime.now().time().hour
    m=int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().time().minute
    return parseMinute(h, m)

print(parseDate())
