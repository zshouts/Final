"""
Program: final.py
Author: Zach Shouts

"""

from breezypythongui import EasyFrame
import random

class Calculator(EasyFrame):
    """Basic calculator program"""

    def __init__(self):
        """Setting up the display window"""
        EasyFrame.__init__(self, title = "Calculator")

        #Initialize the themes list
        themes = ["light", "dark"]

        #Creating the calculator display window
        self.displayField = self.addFloatField(value = 0, row = 0, column = 0,
                                               columnspan = 4)

        #Creating numpad buttons
        #Row 1
        self.sevenbutton = self.addButton(text = "7", row = 1, column = 0,
                                          fg = "black", bg = "white")
        self.sevenbutton.configure(width = 6, height = 2)
        
        self.eightbutton = self.addButton(text = "8", row = 1, column = 1,
                                          fg = "black", bg = "white")
        self.eightbutton.configure(width = 6, height = 2)
        
        self.ninebutton = self.addButton(text = "9", row = 1, column = 2,
                                         fg = "black", bg = "white")
        self.ninebutton.configure(width = 6, height = 2)
        
        self.dividebutton = self.addButton(text = "/", row = 1, column = 3,
                                           fg = "black", bg = "white")
        self.dividebutton.configure(width = 6, height = 2)
        
        #Row 2
        self.fourbutton = self.addButton(text = "4", row = 2, column = 0,
                                         fg = "black", bg = "white")
        self.fourbutton.configure(width = 6, height = 2)

        self.fivebutton = self.addButton(text = "5", row = 2, column = 1,
                                         fg = "black", bg = "white")
        self.fivebutton.configure(width = 6, height = 2)

        self.sixbutton = self.addButton(text = "6", row = 2, column = 2,
                                        fg = "black", bg = "white")
        self.sixbutton.configure(width = 6, height = 2)

        self.multiplybutton = self.addButton(text = "*", row = 2, column = 3,
                                             fg = "black", bg = "white")
        self.multiplybutton.configure(width = 6, height = 2)

        #Row 3
        self.onebutton = self.addButton(text = "1", row = 3, column = 0,
                                        fg = "black", bg = "white")
        self.onebutton.configure(width = 6, height = 2)

        self.twobutton = self.addButton(text = "2", row = 3, column = 1,
                                        fg = "black", bg = "white")
        self.twobutton.configure(width = 6, height = 2)

        self.threebutton = self.addButton(text = "3", row = 3, column = 2,
                                          fg = "black", bg = "white")
        self.threebutton.configure(width = 6, height = 2)

        self.subtractbutton = self.addButton(text = "-", row = 3, column = 3,
                                             fg = "black", bg = "white")
        self.subtractbutton.configure(width = 6, height = 2)

        #Row 4
        self.clearbutton = self.addButton(text = "Clear", row = 4, column = 0,
                                          fg = "black", bg = "white")
        self.clearbutton.configure(width = 6, height = 2)

        self.zerobutton = self.addButton(text = "0", row = 4, column = 1,
                                         fg = "black", bg = "white")
        self.zerobutton.configure(width = 6, height = 2)

        self.decimalbutton = self.addButton(text = ".", row = 4, column = 2,
                                            fg = "black", bg = "white")
        self.decimalbutton.configure(width = 6, height = 2)

        self.additionbutton = self.addButton(text = "+", row = 4, column = 3,
                                             fg = "black", bg = "white")
        self.additionbutton.configure(width = 6, height = 2)

        #Row 5
        #Theme button will change the display from a light or dark theme
        self.themebutton = self.addButton(text = "Dark", row = 5, column = 0,
                                          columnspan = 2,
                                          fg = "black", bg = "white",
                                          command = self.theme(activeTheme))
        
        #Prints info on the program to the python shell
        self.infobutton = self.addButton(text = "Info", row = 5, column = 2,
                                         columnspan = 2,
                                         fg = "black", bg = "white")


                

    def theme(self, activeTheme):
        


      



"""
    def subtraction(self):


    def multiplication(self):


    def division(self):
""" 





def main():
    Calculator()

main()
