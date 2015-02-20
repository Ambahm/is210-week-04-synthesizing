#!usr/bin/env python
# -*- coding: utf-8 -*-

""" TIME CHECK .. DAY CHECK """

DAY_CHECK = ['SAT', 'sat', 'SATURDAY', 'saturday'
             'SUN', 'sun', 'SUNDAY', 'sunday']      # weekends check variable
DAY = raw_input('PLEASE ENTER THE DAY ')
SNOOZE = bool                                       # Setting a boolean variable

TIME_NEW = int(raw_input('PLEASE ENTER THE *4* DIGITS MILITARY TIME '))

if DAY in DAY_CHECK or TIME_NEW < 600:       # if wknd variable or <600
    SNOOZE = True

else:
    print 'Beep! ' * 5
