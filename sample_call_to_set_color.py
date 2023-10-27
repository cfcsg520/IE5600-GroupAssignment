# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:59:00 2023
Filename: sample_call_to_set_color.py
Purpose: To set the text color to be print to console
Version: 1.0
@author: No Name
Function List:
(1) main()
"""
#*****************************************************************

#===========================
#IMPORT EXETERNAL FUNCTIONS
#===========================
import color_palette as cp #Import the color palette and set the alias

#===========================
#VARIABLES
#===========================

#===========================
#LOCAL FUNCTION DEFINITION
#===========================

def main():
    # Example: function call to set_color_text
    set_color = cp.ColoredText()
    
    print(set_color.set_color_text("This text is red.", "RED"))
    print(set_color.set_color_text("This text is black.", "BLACK"))
    print(set_color.set_color_text("This text is green.", "GREEN"))
    print(set_color.set_color_text("This text is yellow.", "YELLOW"))
    print(set_color.set_color_text("This text is blue.", "BLUE"))
    print(set_color.set_color_text("This text is magenta.", "MAGENTA"))
    print(set_color.set_color_text("This text is cyan.", "CYAN"))
    print(set_color.set_color_text("This text is white.", "WHITE"))
     
    # if True:
    #     pass

if __name__ == '__main__': 
        main()
