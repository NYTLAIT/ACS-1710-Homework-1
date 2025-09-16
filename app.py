
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The {adjective} {noun} yelled at everyone in the fridge.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        product = int(number1) * int(number2)
        return f'{number1} times {number2} is {product}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit():
        words = ""
        words += word + " "
        for i in range(int(n)):
            if i < int(n) - 1:
                words += word + " "
        return f'{words}'
    else:
        return f'Invalid input. Please try again by entering a word and a number!'

import random
@app.route('/dicegame')
def dicegame():
    number = random.randint(1, 6)
    if number == 6:
        return f'You rolled a {number}. You won!'
    else:
        return f'You rolled a {number}. You lost!'


if __name__ == '__main__':
    app.run(debug=True)

