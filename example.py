from flask import Flask,render_template,url_for,request,session,redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__,template_folder='../../template')
app.config["MONGO_URI"] = "mongodb+srv://neilakash:omnamah@cluster0.z0t2ojj.mongodb.net/"
mongo = PyMongo(app)    

@app.route('/')
def msg():
    if 'username' in session:
       
     return 'you r logged in: '+ session['username']
    return render_template('login.html')

@app.route('/login', methods=['POST']) 
def login():
   users= mongo.db.users
   login_user= users.find_one({'name':request.form['username']})

   if login_user:
      if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['password'].encode('utf-8')==login_user['password'].encode('utf-8')):
         session['username']= request.form['username']
         return redirect(url_for('login.html'))
      return 'Invalid Username or Password'
   
@app.route('/register',methods= ['POST','GET'])
def register():

      if request.method=='POST':
         users= mongo.db.users
         existing_user=users.find_one({'name':request.form['username']})

         if existing_user is None:
            hashpass= bcrypt.hashpaw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password':hashpass})

         session['username']= request.form('username')
         return  redirect(url_for('login')) 


if __name__== '__main__':
  app.secret_key= 'secretiveagain'

app.run(debug=True )

