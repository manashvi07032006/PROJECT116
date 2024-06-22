from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "SHINCHAN NOHARA" 
    age = "5"
    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():
    name = "HIROSHI NOHARA"
    age = 35
    return render_template('father.html' , name = name, age=age)

@app.route("/mother")
def mother():
    name = "MISAE NOHARA"
    age = 29
    return render_template('mother.html' , name = name, age=age)

@app.route("/sister")
def sister():
    name = "HIMAWARI NOHARA"
    age = 1
    return render_template('sister.html' , name = name, age=age)

@app.route("/friend")
def friend():
    name1 = "KAZAMA"
    name2 = "BOCHAN"
    name3 = "NENE"
    name4 = "MASAO"
    age = 5
    return render_template('friend.html' , name1 = name1, name2 = name2, name3 = name3, name4 = name4, age=age)

if __name__  ==  '__main__':
    app.run(debug=True)