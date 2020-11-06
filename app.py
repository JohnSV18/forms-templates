from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')



@app.route('/froyo_results')
def show_froyo_results():
    context ={
    'users_froyo_toppings' : request.args.get('toppings'),
    'users_froyo_flavor' : request.args.get('flavor')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """
@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fave_color = request.args.get('color')
    users_fave_animal = request.args.get('animal')
    users_fave_city = request.args.get('city')
    return f'Wow, I didnt know {users_fave_color} {users_fave_animal}s lived in {users_fave_city}!'
    

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Insert your secret message<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    secret_mess = sort_letters(request.form['message'])
    
    return 'Here is your secret message: ' + f'{secret_mess}'


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
    'firstnum' : request.args.get('operand1'),
    'secondnum' : request.args.get('operand2'),
    'operator' : request.args.get('operation'),
    'result' : 0
    }
    if (context['operator'] == 'add'):
        context['result'] = int(context['firstnum']) + int(context['secondnum'])
    elif (context['operator'] == "subtract"):
        context['result'] = int(context['firstnum']) - int(context['secondnum'])
    elif (context['operator'] == "divide"):
        context['result'] = int(context['firstnum']) / int(context['secondnum'])
    elif (context['operator'] == "multiply"):
        context['result'] = int(context['firstnum']) * int(context['secondnum'])



    return render_template('calculator_results.html', **context)

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
    debug=True
