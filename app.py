# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
# This initializes the Flask application.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
# Define the endpoint
# This defines a route (or endpoint) /helloworld that will be triggered when a GET request is made.
@app.route('/helloworld', methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    #The function that returns the response "Hello, World!".
    return 'Hello, World!'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    # This starts the app in debug mode, which helps in development by auto-reloading on code changes.
    # Run the Flask application
    app.run(debug=True)

# python app.py -> run this commomnd in terminal to run application
