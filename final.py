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
        self.themes = ["light", "dark"]

        #Initialize the info dictionary
        self.info = {"Author":"Zach Shouts", "Date":"12.08.2020", "Filename":"final.py"}
        
        #Initialize expression variables
        self.expression = "0"
        self.operator = "+"
        self.x = 0
        self.y = 0

        self.file = open("calculatorHistory.txt", 'w')
        
        #Creating the calculator display window
        self.displayField = self.addTextField(text = "0", row = 0, column = 1,
                                              columnspan = 3)

        #Creating the Exit Button
        self.savebutton = self.addButton(text = "Save", row = 0, column = 0,
                                         fg = "black", bg = "white",
                                         command = self.save)
        self.savebutton.configure(width = 6, height = 2)

        #Creating numpad buttons
        #Row 1
        self.sevenbutton = self.addButton(text = "7", row = 1, column = 0,
                                          fg = "black", bg = "white",
                                          command = self.numberSeven) 
        self.sevenbutton.configure(width = 6, height = 2)
        
        self.eightbutton = self.addButton(text = "8", row = 1, column = 1,
                                          fg = "black", bg = "white",
                                          command = self.numberEight)
        self.eightbutton.configure(width = 6, height = 2)
        
        self.ninebutton = self.addButton(text = "9", row = 1, column = 2,
                                         fg = "black", bg = "white",
                                         command = self.numberNine)
        self.ninebutton.configure(width = 6, height = 2)
        
        self.dividebutton = self.addButton(text = "/", row = 1, column = 3,
                                           fg = "black", bg = "white",
                                           command = self.division)
        self.dividebutton.configure(width = 6, height = 2)
        
        #Row 2
        self.fourbutton = self.addButton(text = "4", row = 2, column = 0,
                                         fg = "black", bg = "white",
                                         command = self.numberFour)
        self.fourbutton.configure(width = 6, height = 2)

        self.fivebutton = self.addButton(text = "5", row = 2, column = 1,
                                         fg = "black", bg = "white",
                                         command = self.numberFive)
        self.fivebutton.configure(width = 6, height = 2)

        self.sixbutton = self.addButton(text = "6", row = 2, column = 2,
                                        fg = "black", bg = "white",
                                        command = self.numberSix)
        self.sixbutton.configure(width = 6, height = 2)

        self.multiplybutton = self.addButton(text = "*", row = 2, column = 3,
                                             fg = "black", bg = "white",
                                             command = self.multiplication)
        self.multiplybutton.configure(width = 6, height = 2)

        #Row 3
        self.onebutton = self.addButton(text = "1", row = 3, column = 0,
                                        fg = "black", bg = "white",
                                        command = self.numberOne)
        self.onebutton.configure(width = 6, height = 2)

        self.twobutton = self.addButton(text = "2", row = 3, column = 1,
                                        fg = "black", bg = "white",
                                        command = self.numberTwo)
        self.twobutton.configure(width = 6, height = 2)

        self.threebutton = self.addButton(text = "3", row = 3, column = 2,
                                          fg = "black", bg = "white",
                                          command = self.numberThree)
        self.threebutton.configure(width = 6, height = 2)

        self.subtractbutton = self.addButton(text = "-", row = 3, column = 3,
                                             fg = "black", bg = "white",
                                             command = self.subtraction)
        self.subtractbutton.configure(width = 6, height = 2)

        #Row 4
        self.clearbutton = self.addButton(text = "Clear", row = 4, column = 0,
                                          fg = "black", bg = "white",
                                          command = self.clear)
        self.clearbutton.configure(width = 6, height = 2)

        self.zerobutton = self.addButton(text = "0", row = 4, column = 1,
                                         fg = "black", bg = "white",
                                         command = self.numberZero)
        self.zerobutton.configure(width = 6, height = 2)

        self.decimalbutton = self.addButton(text = ".", row = 4, column = 2,
                                            fg = "black", bg = "white",
                                            command = self.decimal)
        self.decimalbutton.configure(width = 6, height = 2)

        self.additionbutton = self.addButton(text = "+", row = 4, column = 3,
                                             fg = "black", bg = "white",
                                             command = self.addition)
        self.additionbutton.configure(width = 6, height = 2)

        #Row 5
        #Theme button will change the display from a light or dark theme
        self.themebutton = self.addButton(text = "Theme", row = 5, column = 0,
                                          columnspan = 1,
                                          fg = "black", bg = "white",
                                          command = self.theme)

        self.equalsbutton = self.addButton(text = "=", row = 5, column = 1,
                                           columnspan = 2,
                                           fg = "black", bg = "white",
                                           command = self.execute)
        self.equalsbutton.configure(width = 12, height = 2)
        
        #Prints info on the program to the python shell
        self.infobutton = self.addButton(text = "Info", row = 5, column = 3,
                                         columnspan = 1,
                                         fg = "black", bg = "white",
                                         command = self.information)




    def division(self):
        if self.expression == "0":
            self.displayField.setText("Enter a Number First")
        elif self.expression != "0":
            self.x = self.expression
            self.operator = "/"
            self.expression = "0"
            self.displayField.setText("")
        return self.x, self.operator, self.expression

    def multiplication(self):
        if self.expression == "0":
            self.displayField.setText("Enter a Number First")
        elif self.expression != "0":
            self.x = self.expression
            self.operator = "*"
            self.expression = "0"
            self.displayField.setText("")
        return self.x, self.operator, self.expression

    def subtraction(self):
        if self.expression == "0":
            self.expression = "-"
            self.displayField.setText("-")
        elif self.expression != "0":
            self.x = self.expression
            self.operator = "-"
            self.expression = "0"
            self.displayField.setText("")
        return self.x, self.operator, self.expression

    def addition(self):
        if self.expression == "0":
            self.displayField.setText("Enter a Number First")
        elif self.expression != "0":
            self.x = self.expression
            self.expression = "0"
            self.displayField.setText("")
        return self.x, self.expression

    def decimal(self):
        if self.expression == "0":
            self.expression = "0."
            self.displayField.setText("0.")
        elif self.expression != "0":
            self.expression = self.expression + "."
            self.displayField.setText(self.expression)
        return self.expression

    def clear(self):
        self.expression = "0"
        self.displayField.setText("0")
        return self.expression

    def theme(self):
        activeTheme = "light"
        if activeTheme == "light":
            print("light")
        elif activeTheme == "dark":
            print("dark")

    def numberZero(self):
        if self.expression == "0":
            self.displayField.setText("0")
        elif self.expression != "0":
            self.expression = self.expression + "0"
            self.displayField.setText(self.expression)
        return self.expression

    def numberOne(self):
        if self.expression == "0":
            self.expression = "1"
            self.displayField.setText("1")
        elif self.expression != "0":
            self.expression = self.expression + "1"
            self.displayField.setText(self.expression)
        return self.expression

    def numberTwo(self):
        if self.expression == "0":
            self.expression = "2"
            self.displayField.setText("2")
        elif self.expression != "0":
            self.expression = self.expression + "2"
            self.displayField.setText(self.expression)
        return self.expression

    def numberThree(self):
        if self.expression == "0":
            self.expression = "3"
            self.displayField.setText("3")
        elif self.expression != "0":
            self.expression = self.expression + "3"
            self.displayField.setText(self.expression)
        return self.expression

    def numberFour(self):
        if self.expression == "0":
            self.expression = "4"
            self.displayField.setText("4")
        elif self.expression != "0":
            self.expression = self.expression + "4"
            self.displayField.setText(self.expression)
        return self.expression

    def numberFive(self):
        if self.expression == "0":
            self.expression = "5"
            self.displayField.setText("5")
        elif self.expression != "0":
            self.expression = self.expression + "5"
            self.displayField.setText(self.expression)
        return self.expression

    def numberSix(self):
        if self.expression == "0":
            self.expression = "6"
            self.displayField.setText("6")
        elif self.expression != "0":
            self.expression = self.expression + "6"
            self.displayField.setText(self.expression)
        return self.expression

    def numberSeven(self):
        if self.expression == "0":
            self.expression = "7"
            self.displayField.setText("7")
        elif self.expression != "0":
            self.expression = self.expression + "7"
            self.displayField.setText(self.expression)
        return self.expression

    def numberEight(self):
        if self.expression == "0":
            self.expression = "8"
            self.displayField.setText("8")
        elif self.expression != "0":
            self.expression = self.expression + "8"
            self.displayField.setText(self.expression)
        return self.expression

    def numberNine(self):
        if self.expression == "0":
            self.expression = "9"
            self.displayField.setText("9")
        elif self.expression != "0":
            self.expression = self.expression + "9"
            self.displayField.setText(self.expression)
        return self.expression
        
    def execute(self):
        self.y = self.expression
        self.x = int(self.x)
        self.y = int(self.y)
        result = 0
        if self.operator == "+":
            result = self.x + self.y
            self.displayField.setText(result)
            self.expression = result
        elif self.operator == "-":
            result = self.x - self.y
            self.displayField.setText(result)
            self.expression = result
        elif self.operator == "*":
            result = self.x * self.y
            self.displayField.setText(result)
            self.expression = result
        elif self.operator == "/":
            try:
                result = self.x / self.y
                self.displayField.setText(result)
                self.expression = result
            except:
                self.displayField.setText("Error")
        self.file.write(str(self.x) + self.operator + str(self.y) + "=" + str(result) + '\n')
        return self.expression
            

    def information(self):
        print("Author: " + self.info["Author"])
        print("Date created: " + self.info["Date"])
        print("Filename: " + self.info["Filename"])


    def save(self):
        self.file.close()
        


def main():
    Calculator()

main()
