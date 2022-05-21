from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# import statements, maybe some other routes

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name, num):
    print(name, num)
    return "Hello, " + name * num

    
if __name__=="__main__": # Ensure this file is being run directly and not from a different module 
# app.run(debug=True) should always be the very last statement! 
    app.run(debug=True, port=5001)    # Run the app in debug mode. set to false when deploying


