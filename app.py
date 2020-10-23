from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user"""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route("/SeaCucumber")
def sea_cucumber():
    return "My favorite animal is a Sea Cucumber"

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
        return number1 + " Times " + number2 + " is " + str((int(number1)*int(number2)))
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

if __name__ == "__main__":
    app.run(debug=True)