"""
Module providing webpage initialization.

Functions:
    start()
        Receives user input and calls appropriate calculation method.

Variables:
    app: Flask
    """

from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)


@app.route('/calculate')
def start():  # put application's code here
    """Function requesting user input and calling appropriate calculation method."""
    #Requesting input parameters from user:
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    # Initializing calculator instance:
    calculator = Calculator(arg1, arg2)

    #Determining appropriate return based on provided input:
    match op:
        case 'sum':
            return f'{arg1} + {arg2} = ' + str(calculator.sum())
        case 'subtract':
            return f'{arg1} - {arg2} = ' + str(calculator.subtract())
        case 'multiply':
            return f'{arg1} * {arg2} = ' + str(calculator.multiply())
        case 'divide':
            return f'{arg1} : {arg2} = ' + str(calculator.divide())
        case _:
            return 'Error'



if __name__ == '__main__':
    app.run()
