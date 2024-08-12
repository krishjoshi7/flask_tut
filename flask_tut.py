#importing dependencies 
"""we are using redirect to redirect  the user from a certain page
to redriect we return rediect followed by the url_for with in it followed by the name of function
now we wil use render web page by using render_template this allow us to render html page"""

from flask import Flask, redirect,url_for, render_template

#intialise the app
app =Flask(__name__)


#defining function for home page
#falsk does not know where to go and get this page so we give it a route 
# / is for the path to get the function 



@app.route('/<name>')
def home(name):
    return render_template("index.html", content=name, r="You are doing great")


#creating another page 
@app.route('/<name>')
def user(name):
    return f'Hello {name}!'


#creating admin page 
@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__ =='__main__':
    app.run()