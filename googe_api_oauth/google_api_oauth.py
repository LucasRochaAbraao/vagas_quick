#!/usr/bin/env python3
"""
[Documentation here]
                             } (
Author: Lucas Rocha Abraão  (   ) )
Date: [date]                 ) { (
License: GNU GPLv3        ___|___)_
                       .-'---------|
                      ( C|/\/\/\/\/|
                       '-./\/\/\/\/|
                         '_________'
                          '-------'
"""

import gspread

gc = gspread.oauth()

sh = gc.open("TESTE")

print(sh.sheet1.get("A1"))
