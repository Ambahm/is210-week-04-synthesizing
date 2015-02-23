#!usr/bin/env python
# -*- coding: utf-8 -*-

""" TIME CHECK .. DAY CHECK """

DAY_CHECK = ['SAT', 'sat', 'SATURDAY', 'saturday'
             'SUN', 'sun', 'SUNDAY', 'sunday']      # weekends check variable
DAY = raw_input('PLEASE ENTER THE DAY ')

TIME_NEW = int(raw_input('PLEASE ENTER THE *4* DIGITS MILITARY TIME '))

if DAY is DAY_CHECK or TIME_NEW < 600:       # if wknd variable or <600
    SNOOZE = True                            # Setting a boolean variable

else:
    print 'Beep! ' * 5
