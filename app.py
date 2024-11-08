"""Module providing webpage initialization and basic functionality of the web calculator."""

from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def hello_world():  # put application's code here
    """Function performing mathematical operations based on user input."""
    #Requesting input parameters from user:
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    #Determining appropriate return based on provided input:
    match op:
        case 'sum':
            return f'{arg1} + {arg2} = ' + str(arg1 + arg2)
        case 'subtract':
            return f'{arg1} - {arg2} = ' + str(arg1 - arg2)
        case 'multiply':
            return f'{arg1} * {arg2} = ' + str(arg1 * arg2)
        case 'divide':
            return f'{arg1} : {arg2} = ' + str(arg1 / arg2)
        case _:
            return 'Error'



if __name__ == '__main__':
    app.run()
