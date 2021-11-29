class Calculator:
    # empty constructor
    def __init__(self):
        pass

    def add(self, a, b):
        try:
            return a + b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')


    def multiply(self, a, b):
        try:
            return a * b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')

    def subtract(self, a, b):
        try:
            return a - b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')

    def divide(self, a, b):
        try:
            if a != 0:
                return a / b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')

    def modul_o(self, a, b):
        try:
            if a != 0:
                return a % b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')

    def fraction(self, a, b):
        try:
            if a != 0:
                return a // b
        except TypeError as te:
            print(f'An Error occured : {te} ')
        except ArithmeticError as ae:
            print(f'An Error occured : {ae} ')
        except ValueError as ve:
            print(f'An Error occured : {ve} ')

