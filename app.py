from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/contact',methods =["GEt","POST"])
def contactus():
    if request.method=='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        country = request.form.get("country")
        state = request.form.get("state")
        message = request.form.get("message")
        print(name,email,country,state,message)
        conn = sqlite3.connect('contactus.db')
        cur = conn.cursor()
        cur.execute(f'''
        INSERT INTO CONTACT VALUES(
                    "{name}","{email}",
                    "{country}","{state}",
                    "{message}"           
        )
        ''')
        conn.commit()
        return render_template("message.html")
    else:
        return render_template('contactus.html')    

    
    
if __name__=='__main__':
    app.run()