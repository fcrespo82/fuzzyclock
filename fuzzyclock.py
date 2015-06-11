#! /usr/bin/env python
# coding: utf-8

import datetime
import sys

def switch(choice, case_list, default):
    for the_range, the_response in case_list:
        if choice in the_range:
            return the_response()
    return default

def parse_hour(hour):
    hour_list = ("uma", "duas", "tres", "quatro", "cinco", "seis", "sete",
                 "oito", "nove", "dez", "onze", "meio dia")

    return "meia noite" if hour == 24 else hour_list[(hour%12)-1]

def junction(hour):
    junction_list = [
        ([1, 13, 24, 25], lambda: " a "),
        ([12], lambda: " o "),
    ]

    return switch(hour, junction_list, " as ")

def parse_time(hour, minute):
    minute_list = [
        (range(3, 8), lambda: parse_hour(hour) + " e cinco"),
        (range(8, 13), lambda: parse_hour(hour) + " e dez"),
        (range(13, 18), lambda: parse_hour(hour) + " e quinze"),
        (range(18, 23), lambda: parse_hour(hour) + " e vinte"),
        (range(23, 28), lambda: parse_hour(hour) + " e vinte e cinco"),
        (range(28, 33), lambda: parse_hour(hour) + " e meia"),
        (range(33, 38), lambda: parse_hour(hour) + " e trinta e cinco"),
        (range(38, 43), lambda: "vinte para" + junction(hour + 1) + parse_hour(hour + 1)),
        (range(43, 48), lambda: "quinze para" + junction(hour + 1) + parse_hour(hour + 1)),
        (range(48, 53), lambda: "dez para" + junction(hour + 1) + parse_hour(hour + 1)),
        (range(53, 58), lambda: "cinco para" + junction(hour + 1) + parse_hour(hour + 1)),
        (range(58, 60), lambda: parse_hour(hour + 1)),
        (range(0, 3), lambda: parse_hour(hour)),
    ]

    return switch(minute, minute_list, parse_hour(hour))

def main():
    the_hour = int(sys.argv[1]) if len(sys.argv) > 2 else datetime.datetime.now().time().hour
    the_minute = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().time().minute
    print(parse_time(the_hour, the_minute))

main()
