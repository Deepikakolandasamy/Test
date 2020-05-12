
# coding: utf-8

# In[2]:


from flask import Flask, flash, redirect, render_template, request, session
import random

app = Flask(__name__, template_folder='flask_template')
error=''
message="e"


@app.route('/',methods=['GET'])
def home():
    return render_template('angle.html',message=message)

@app.route('/user',methods=['POST'])
def reset():
    hour=request.form['hour']
    minute=request.form['minute']
    if ((hour>=0 & hour<=12) & (minute>=0 & minute<=60):
        message=abs((hour * 30 + minute * 0.5)-(minute * 6))
        return home()+message
            
     else:
        message='Enter correct time'
        return home()+message
             


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0')




