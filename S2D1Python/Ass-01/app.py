
from flask import Flask

app = Flask(__name__)

# Route for the Welcome Message at "/"
@app.route('/')
def sayHello():
    return "Welcome To Python Flask Learning"


# Rout for the greeting with name

@app.route('/greet/<username>')
def sayHelloTo(username):
    return f"Hello {username}!"


# Rout for the goodbye

@app.route('/farewell/<username>')
def sayFarewell(username):
    return f"GoodBye {username}!"

if __name__== '__main__':
    app.run(debug=True)

# from flask import Flask

# # Create a Flask web app
# app = Flask(__name__)

# # Route for the welcome message at '/'
# @app.route('/')
# def welcome():
#     return "Welcome to the Flask application!"

# # Route for greeting a user at '/greet/<username>'
# @app.route('/greet/<username>')
# def greet(username):
#     return f"Hello, {username}!"

# # Route for saying farewell to a user at '/farewell/<username>'
# @app.route('/farewell/<username>')
# def farewell(username):
#     return f"Goodbye, {username}!"

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Flask World!'

# # if __name__ == '__main__':
#     app.run(debug=True)
