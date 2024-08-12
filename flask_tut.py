#importing dependencies 
"""we are using redirect to redirect  the user from a certain page
to redriect we return rediect followed by the url_for with in it followed by the name of function"""

from flask import Flask, redirect,url_for

#intialise the app
app =Flask(__name__)


#defining function for home page
#falsk does not know where to go and get this page so we give it a route 
# / is for the path to get the function 



@app.route('/')
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"


#creating another page 
@app.route('/<name>')
def user(name):
    return f'Hello {name}!'


#creating admin page 
@app.route('/')
def admin():
    return redirect(url_for("home"))


if __name__ =='__main__':
    app.run()