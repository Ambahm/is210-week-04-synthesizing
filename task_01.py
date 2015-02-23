#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Nested if else- multiple choices"""


ACC_COL = ['Ceramic Glaze', 'Cumulus Nimbus',
           'Platinum Mist', 'Spartan Sage']     # Accent list

BASE_COL = ['Seattle Gray', 'Manatee']          # Base color listing

HLT_COL = ['Basically White', 'White', 'Off White',
           'Paper White', 'Bone White', 'Just White',
           'Fractal Whte', 'Not White']         # HIghlight color list

print 'BASE COLORS      :', BASE_COL
print 'ACCENTCOLORS     :', ACC_COL
print 'HIGHLIGHT COLORS :', HLT_COL

BASE = raw_input('\nEnter Choice of BASE Color :')

NEWS = '\nYour selected colors are: {}, {} and {}!'  # OUTPUT

if BASE == BASE_COL[0]:                     # Seattle Gray Base
    ACCENT = raw_input('\nEnter Choice of ACCENT Color : ')
    if ACCENT == ACC_COL[0]:
        HIGHLIGHT = raw_input('Enter Choice of HIGHLIGHT Color : ')
        if HIGHLIGHT == HLT_COL[0]:         # Ceramic, Bas-White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == HLT_COL[1]:       # Ceramic,  White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)

    elif ACCENT == ACC_COL[1]:
        HIGHLIGHT = raw_input('\nEnter Choice of HIGHLIGHT Color : ')
        if HIGHLIGHT == HLT_COL[2]:         # CNimbus, Off-White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == HLT_COL[3]:       # CNimbus, Paper-White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)

elif BASE == BASE_COL[1]:                   # Manatee Base Color
    ACCENT = raw_input('\nEnter Choice of ACCENT Color : ')
    if ACCENT == ACC_COL[2]:                # P.Mist, Bone-White
        HIGHLIGHT = raw_input('\nEnter Choice of HIGHLIGHT Color : ')
        if HIGHLIGHT == HLT_COL[4]:
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == HLT_COL[5]:       # P.Mist, Just White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)

    if ACCENT == ACC_COL[3]:
        HIGHLIGHT = raw_input('\nEnter Choice of HIGHLIGHT Color : ')
        if HIGHLIGHT == HLT_COL[6]:         # S.Sage, Fractal White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == HLT_COL[7]:       # S.Sage, Not White
            print NEWS.format(BASE, ACCENT, HIGHLIGHT)
