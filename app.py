from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user"""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route("/SeaCucumber")
def sea_cucumber():
    return "My favorite animal is a Sea Cucumber"

@app.route("/penguins")
def penguins():
    return "Penguins are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return "How did you know I liked " + users_dessert +"?"

@app.route("/madlibs/<adjective>/<noun>")
def new_madlib(adjective,noun):
    return "The " + adjective + " " + noun + " jumped into the fishtank!"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    if number1.isdigit() is True and number2.isdigit() is True:
        return number1 + " times " + number2 + " is " + str((int(number1)*int(number2)))+"."
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word,n):
    output = ''
    for _ in range(0,int(n)):
        output += ' '+word+':'+str(_+1)
    return output

@app.route('/reverse/<string>')
def reverse_string(string):
    current = len(string)
    output = ''
    for _ in range(0,current):
        output += string[current-1]
        current-=1
    return output

@app.route('/dicegame')
def dice_game():
    computer_roll = random.randint(1,6)
    player_roll = random.randint(1,6)
    if computer_roll > player_roll:
        output = f"You rolled a {player_roll} and lost. The computer rolled a {computer_roll}."
        return output
    elif computer_roll<player_roll:
        output = f"You rolled a {player_roll} and WON! The computer rolled a {computer_roll}."
        return output
    else:
        output = f"You Tied! Your roll:{player_roll} Computer roll:{computer_roll}"
        return output


if __name__ == "__main__":
    app.run(debug=True)