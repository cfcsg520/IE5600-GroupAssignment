# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:59:00 2023
Filename: color_palette.py
Purpose: To set the text color to be print to console
Version: 1.0
@author: No Name
Function List:
(1) class ColorText()

"""
#*****************************************************************

class ColoredText:
    # ANSI escape codes for text colors
    TEXT_COLOR = {
        "BLACK": "\033[30;1m",
        "RED": "\033[31;1m",
        "GREEN": "\033[32;1m",
        "YELLOW": "\033[33;1m",
        "BLUE": "\033[34;1m",
        "MAGENTA": "\033[35;1m",
        "CYAN": "\033[36;1m",
        "WHITE": "\033[37;1m",
    }

    # ANSI escape code to reset colors and formatting
    RESET = "\033[0m"

    @classmethod
    def set_color_text(cls, text, color):
        if color.upper() in cls.TEXT_COLOR:
            return cls.TEXT_COLOR[color.upper()] + text + cls.RESET
        else:
            return text
