from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://neilakash:omnamah@cluster0.z0t2ojj.mongodb.net/"
mongo = PyMongo(app)    

@app.route('/')
def registration():
    return 'registration.html'



app.run(debug=True, port=5000)