from flask import Flask, render_template


#create a flask instance

app= Flask(__name__)

#create a route decorator

@app.route('/')

# def index():
# 	return "<h1>Hello World!</h1>"
#localhost:5000/user/john

def index():
	first_name="john"
	stuff="This is bold text"

	fav_pizza=["pepparoni","cheese",41]
	return render_template("index.html",
		first_name=first_name,
		stuff=stuff,fav_pizza=fav_pizza)

@app.route ("/user/<name>")


def user(name):
	return render_template("user.html",name=name)
	


#create custom error pages

#invalid url

@app.errorhandler(404)
def page_not_found(e): 
	return render_template("404.html"),404

#invalid url

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500	

