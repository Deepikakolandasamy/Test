
# coding: utf-8

# In[1]:




# In[2]:


from flask import Flask, flash, redirect, render_template, request, session
import random
import os
app = Flask(__name__, template_folder='flask_template')
error=''
message="e"


@app.route('/',methods=['GET'])
def home():
    return render_template('angle.html',message=message)

@app.route('/user',methods=['POST'])
def reset():
    try:
        hour=int(request.form['hour'])
        minute=int(request.form['minute'])
        if (((hour >= 0) & (hour <= 12)) & ((minute >= 0) & (minute <= 60))):
            angle=abs((hour * 30 + minute * 0.5)-(minute * 6))
            message="Angle between the hour and minute: "+str(angle)
            return render_template('angle.html',message=message)    
        else:
            message='Enter correct time'
            return render_template('angle.html',message=message)
    except:
        message = "Enter some interger value"
        return render_template('angle.html',message=message)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0')





